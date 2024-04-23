<script context="module" lang="ts">
  import { getCookie } from "./cookies.svelte";

  export async function checkAuth() {
    try {
      let accessToken = getCookie("accessToken");
      if (accessToken) {
        let auth_url = `http://localhost:5000/api/auth`;
        let response = await fetch(auth_url, {
          credentials: "include",
        });
        let data = await response.json();
        return data.id;
      } else {
        return false;
      }
    } catch (error) {
      console.log(error);
      return false;
    }
  }
</script>
