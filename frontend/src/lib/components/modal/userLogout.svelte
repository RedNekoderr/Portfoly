<script lang="ts">
  import { redirect } from "../functions/redirect.svelte";
  import { deleteCookie } from "../functions/cookies.svelte";
  async function logout() {
    const response = await fetch("http://localhost:5000/api/logout");
    if (response.ok) {
      deleteCookie("accessToken");
      redirect("/login");
    }
  }
</script>

<section>
  <div class="container">
    <div class="row">
      <div
        class="col d-flex flex-column justify-content-center align-items-center mt-5"
      >
        <h1 class="text title">Logout</h1>
        <button on:click={logout} class="btn btn-danger">Logout</button>
      </div>
    </div>
  </div>
</section>
