<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { Upload } from "svelte-bootstrap-icons";
  import { onMount } from "svelte";
  import { checkAuth } from "../functions/auth.svelte";

  const dispatch = createEventDispatcher();

  export let username: string;
  export let contentType: string;
  export let content: string;

  async function handleSubmit(event: any) {
    const formData = new FormData();
    formData.append("username", username);
    formData.append(contentType, event.target.file.files[0]);

    let fetch_url = `http://localhost:5000/api/set/user-info`;
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

  onMount(() => {
    const fileInput = document.getElementById("file") as HTMLInputElement;

    if (fileInput) {
      fileInput.addEventListener("change", (event: Event) => {
        const files = (event.target as HTMLInputElement).files;
        if (files) {
          const selectedFile = files[0];
          content = URL.createObjectURL(selectedFile);
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
      <h2 class="text text-center">
        Update {contentType.charAt(0).toUpperCase() + contentType.slice(1)}
      </h2>
      <div class="row h-100">
        <div class="col mt-3 d-flex flex-column align-items-center">
          <div
            class="image-container w-100 h-100 d-flex align-items-center m-0 p-0"
            style="background-image: url({content});"
          >
            <img
              class="card-img-top m-0 p-0"
              src={content}
              alt="{username}'s content"
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
          <button type="submit" class="btn mt-4 btn-primary w-25">Update</button
          >
        </div>
      </div>
    </div>
  </form>
</section>

<style>
  label {
    font-size: 1.2em;
  }

  input {
    transition: filter 0.2s ease;
  }

  ::placeholder {
    color: var(--muted);
  }

  label,
  input,
  input:focus,
  ::file-selector-button {
    color: var(--text);
  }

  input,
  input:focus,
  ::file-selector-button {
    background-color: var(--base);
  }

  input:hover,
  input:focus {
    filter: brightness(1.05);
  }

  .image-container {
    position: relative;
    overflow: hidden;
    border-radius: 1em;
    max-height: 350px;
    max-width: 60%;
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
    top: 175px;
    color: var(--text);
    background-color: var(--panel);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 1em;
    cursor: pointer;
  }
</style>
