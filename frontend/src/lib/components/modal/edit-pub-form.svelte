<script lang="ts">
  import { getCookie } from "../functions/cookies.svelte";
  import { createEventDispatcher } from "svelte";
  import { Upload } from "svelte-bootstrap-icons";
  import { onMount } from "svelte";
  import { checkAuth } from "../functions/auth.svelte";
  import type { Publication } from "../types/publication.svelte";
  import { genFormData } from "../functions/genPubForm.svelte";

  const dispatch = createEventDispatcher();
  let username = getCookie("username");

  export let publication: Publication;

  async function handleSubmit(event: any) {
    const formData = genFormData(event, username, publication);
    let fetch_url = `http://localhost:5000/api/set/user-info/update-publication`;
    const auth = await checkAuth();
    if (!auth) {
      console.log("Try again");
      return;
    }
    const response = await fetch(fetch_url, {
      method: "POST",
      body: formData,
      credentials: "include",
    });

    if (response.ok) {
      dispatch("componentUpdate");
      console.log("Success file uploading");
    } else {
      console.error("Failed to upload files");
    }
  }

  async function removePublication(id: number) {
    const auth = await checkAuth();
    if (!auth) {
      console.log("Try again");
      return;
    }
    let fetch_url = `http://localhost:5000/api/del/user/publication?id=${id}`;
    const response = await fetch(fetch_url, {
      method: "GET",
      credentials: "include",
    });
    if (response.ok) {
      dispatch("componentUpdate", "removePublication");
    }
  }

  onMount(() => {
    const fileInput = document.getElementById("file") as HTMLInputElement;

    if (fileInput) {
      fileInput.addEventListener("change", (event: Event) => {
        const files = (event.target as HTMLInputElement).files;
        if (files) {
          const selectedFile = files[0];
          publication.blob = URL.createObjectURL(selectedFile);
          console.log("Selected file:", selectedFile);
        }
      });
    }
  });
</script>

<section class="h-100 container">
  <form
    on:submit={handleSubmit}
    class="row d-flex align-items-center justify-content-center p-3"
  >
    <div class="col d-flex flex-column p-0">
      <h2 class="text">Edit Publication</h2>
    </div>
    <div class="row">
      <div class="col-sm-1 me-2 d-flex flex-column align-items-start">
        <div class="mb-3 mt-1">
          <label for="title" class="">Title</label>
        </div>
        <div class="mb-3 mt-2">
          <label for="short_desc" class="">Snippet</label>
        </div>
        <div class="mb-3 mt-2">
          <label for="type" class="">Type</label>
        </div>
      </div>
      <div class="col-sm-5 d-flex flex-column align-items-start">
        <div class="mb-3 w-75">
          <input
            type="text"
            name="title"
            id="title"
            bind:value={publication.title}
            placeholder="Title"
            class="form-control"
          />
        </div>
        <div class="mb-3 w-75">
          <input
            type="text"
            name="short_desc"
            bind:value={publication.shortDesc}
            placeholder="Short Description"
            class="form-control"
          />
        </div>
        <div class="mb-3 w-75">
          <select
            bind:value={publication.pubType}
            class="form-select"
            name="type"
            id="type"
          >
            <option value="it">IT</option>
            <option value="art">Art</option>
            <option value="article">Article</option>
          </select>
        </div>
      </div>
      <div class="col">
        <div class="row h-100">
          <div class="col d-flex flex-column align-items-center">
            <div
              class="image-container w-100 h-100 d-flex align-items-center m-0 p-0"
              style="background-image: url({publication.blob});"
            >
              <img
                class="card-img-top m-0 p-0"
                src={publication.blob}
                alt="Publication {publication.title}"
              />
            </div>
            <label for="file" class="file-input">
              <Upload width="40" height="40" />
              <input
                type="file"
                name="file"
                id="file"
                accept="image/*"
                style="display: none;"
              />
            </label>
          </div>
        </div>
      </div>
    </div>
    <div class="mb-3 p-0">
      <label for="longDescription" class="form-label text subtle"
        >Description</label
      >
      <textarea
        bind:value={publication.longDesc}
        class="form-control text"
        id="longDescription"
        name="longDescription"
        placeholder="Edit description using Markdown syntax"
        rows="14"
        required
      ></textarea>
    </div>
    <div class="row d-flex flex-row align-items-center justify-content-end">
      <button
        type="button"
        class="btn btn-danger w-25 me-3"
        on:click={() => {
          removePublication(publication.pubID);
        }}
        >Delete
      </button>
      <button type="submit" class="btn btn-primary w-25">Update</button>
    </div>
  </form>
</section>

<style>
  textarea {
    resize: none;
    max-height: 415px;
  }

  textarea,
  img {
    border-radius: 20px;
  }

  label,
  textarea {
    font-size: 1.2em;
  }

  select,
  input {
    transition: filter 0.2s ease;
  }

  ::placeholder,
  textarea:placeholder-shown {
    color: var(--muted);
  }

  label,
  select,
  input,
  input:focus,
  textarea:focus,
  ::file-selector-button {
    color: var(--text);
  }

  input,
  select,
  textarea,
  input:focus,
  select:focus,
  textarea:focus,
  ::file-selector-button {
    background-color: var(--base);
  }

  input:hover,
  input:focus,
  select:hover,
  select:focus,
  textarea:focus {
    filter: brightness(1.05);
  }

  .image-container {
    position: relative;
    overflow: hidden;
    border-radius: 1em;
    max-height: 150px;
  }

  .image-container::before {
    content: "";
    position: absolute;
    background-size: cover;
    background-repeat: no-repeat;
    background-image: inherit;
    filter: brightness(0.7) blur(5px);
    height: 100%;
    width: 100%;
  }

  .image-container img {
    position: relative;
    border-radius: 1em;
  }

  .file-input {
    position: absolute;
    top: 90px;
    color: var(--text);
    background-color: var(--panel);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 1em;
    cursor: pointer;
  }
</style>
