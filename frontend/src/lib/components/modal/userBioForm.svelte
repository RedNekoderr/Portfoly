<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { onMount } from "svelte";
  import { checkAuth } from "../functions/auth.svelte";

  export let username: string;
  export let bio: string;
  const dispatch = createEventDispatcher();

  async function handleSubmit(event: any) {
    const formData = new FormData();
    formData.append("username", username);
    formData.append("description", bio);
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
</script>

<section class="h-100 container">
  <form
    on:submit={handleSubmit}
    class="row d-flex align-items-center justify-content-center p-3"
  >
    <div class="col d-flex flex-column p-0">
      <h2 class="text">Edit Bio</h2>
    </div>
    <div class="mb-3 p-0">
      <textarea
        bind:value={bio}
        class="form-control text"
        id="longDescription"
        name="longDescription"
        placeholder="Bio"
        rows="14"
        required
      ></textarea>
    </div>
    <div class="row d-flex flex-row align-items-center justify-content-end">
      <button type="submit" class="btn btn-primary w-25">Update</button>
    </div>
  </form>
</section>

<style>
  textarea {
    resize: none;
    max-height: 415px;
  }

  textarea {
    border-radius: 20px;
  }

  textarea {
    font-size: 1.2em;
  }

  ::placeholder,
  textarea:placeholder-shown {
    color: var(--muted);
  }

  textarea:focus,
  ::file-selector-button {
    color: var(--text);
  }

  textarea,
  textarea:focus,
  ::file-selector-button {
    background-color: var(--base);
  }

  textarea:focus {
    filter: brightness(1.05);
  }
</style>
