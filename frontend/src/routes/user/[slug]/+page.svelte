<script lang="ts">
  import Navbar from "$lib/components/navbar.svelte";
  import UserPage from "$lib/components/user-page.svelte";

  import { page } from "$app/stores";
  $: slug = $page.params.slug;
</script>

<Navbar />
<UserPage username={slug} />
