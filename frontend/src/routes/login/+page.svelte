<script lang="ts">
  import { onMount } from "svelte";
  import { setCookie } from "$lib/components/functions/cookies.svelte";
  import { checkAuth } from "$lib/components/functions/auth.svelte";
  import { redirect } from "$lib/components/functions/redirect.svelte";
  import Navbar from "$lib/components/navbar.svelte";

  let isAuthorized: boolean = false;
  let username: string;
  let password: string;
  let viewportWidth: number;

  onMount(async () => {
    viewportWidth = window.innerWidth;
    isAuthorized = await checkAuth();
    if (isAuthorized) {
      redirect("profile");
    }
  });

  const login = async () => {
    try {
      let response = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: {
          Accept: "application/json, text/javascript, */*; q=0.01",
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify({ username: username, password: password }),
      });
      let data = await response.json();
      if (data.auth == true) {
        setCookie("username", data.username, 15, false);
        isAuthorized = true;
        redirect("profile");
      }
    } catch (error) {
      console.log(error);
    }
  };
</script>

<Navbar />
<section class="vh-100 d-flex align-items-center">
  <div class={`${viewportWidth > 600 ? "w-50" : ""} container`} id="main">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h2 class="text-center text title-unfree mt-5">Sign in</h2>
            <form class="px-3" on:submit|preventDefault={login}>
              <div class="mt-5">
                <input
                  type="text"
                  class="form-control"
                  id="username"
                  placeholder="Username"
                  required
                  bind:value={username}
                />
              </div>
              <div class="mt-3">
                <input
                  type="password"
                  class="form-control"
                  id="password"
                  placeholder="Password"
                  required
                  bind:value={password}
                />
              </div>
              <div class="d-grid">
                <button type="submit" class="btn btn-primary mt-5 submit-btn"
                  >Sumbit</button
                >
              </div>
            </form>
            <div class="mt-2 mb-5 text-center">
              <a href="/register" class="text button subtle">Sign up</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  section {
    background: url("images/login-bg.jpg");
    background-size: cover;
  }

  .card {
    border-radius: 5%;
    background-color: var(--panel);
  }

  .form-control {
    background-color: var(--base);
    color: var(--text);
  }

  .close-btn {
    margin: 0;
    color: var(--rose);
    transition: color 0.3s ease;
  }

  .close-btn:hover {
    color: var(--red);
  }

  .submit-btn {
    background-color: var(--pine);
    border: none;
  }

  .submit-btn:clicked,
  .btn-primary:hover {
    background-color: var(--iris) !important;
  }

  input {
    background-color: var(--base);
  }
</style>
