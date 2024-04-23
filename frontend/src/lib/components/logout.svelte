<script context="module" lang="ts">
  import { redirect } from "./functions/redirect.svelte";

  export async function logout() {
    await fetch("http://localhost:5000/api/logout", {
      credentials: "include",
    });
    await redirect("home");
  }
</script>

<button on:click={logout} class="btn btn-danger">Logout</button>
