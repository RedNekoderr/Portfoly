<script lang="ts">
  import { getCookie } from "../functions/cookies.svelte";
  import { createEventDispatcher } from "svelte";
  import { checkAuth } from "../functions/auth.svelte";
  import type { Publication } from "../types/publication.svelte";
  import { createPublication } from "../types/publication.svelte";
  import { genFormData } from "../functions/genPubForm.svelte";

  const dispatch = createEventDispatcher();
  let username = getCookie("username");

  let publication: Publication = createPublication(
    0,
    "",
    "",
    "article",
    "",
    "",
    "",
  );
  async function handleSubmit(event: any) {
    const formData = genFormData(event, username, publication);

    const auth = await checkAuth();
    if (!auth) {
      console.log("Try again");
      return;
    }

    let fetch_url = `http://localhost:5000/api/set/user-info/add-publication`;
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
</script>

<section class="h-100 container">
  {#if publication}
    <form
      on:submit|preventDefault={handleSubmit}
      class="row d-flex align-items-center justify-content-center p-3"
    >
      <div class="col d-flex flex-column p-0">
        <h2 class="text">New Publication</h2>
        <div class="mb-3">
          <input
            type="text"
            name="title"
            id="title"
            bind:value={publication.title}
            placeholder="Title"
            class="form-control"
          />
        </div>
        <div class="mb-3">
          <input
            type="text"
            name="short_desc"
            bind:value={publication.shortDesc}
            placeholder="Short Description"
            class="form-control"
          />
        </div>
      </div>
      <div class="mb-3 d-flex row p-0">
        <div class="d-flex col align-items-center text subtle select-section">
          <label for="type" class="me-2">Type</label>
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
        <input
          type="file"
          name="file"
          id="file"
          accept="image/*"
          class="form-control col-sm"
        />
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
      <button type="submit" class="btn btn-primary">Send</button>
    </form>
  {/if}
</section>

<style>
  textarea {
    resize: none;
    border-radius: 20px;
    max-height: 415px;
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
</style>
