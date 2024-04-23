<script lang="ts">
  import { checkAuth } from "$lib/components/functions/auth.svelte";
  import Navbar from "$lib/components/navbar.svelte";
  import UserPage from "$lib/components/user-page.svelte";
  import ContentEdit from "$lib/components/modal/contentEdit.svelte";
  import { Modal } from "svelte-simple-modal";
  import CustomCloseButton from "$lib/components/modal/customCloseButton.svelte";

  import { onMount } from "svelte";
  import { goto } from "$app/navigation";
  import { browser } from "$app/environment";

  let isAuthorized: boolean;
  let updateUserPage: any;

  onMount(async () => {
    isAuthorized = await checkAuth();
    if (!isAuthorized && browser) {
      goto("/login");
    }
  });
</script>

<Navbar />
{#if isAuthorized}
  <UserPage
    bind:updateInfoOnContentChange={updateUserPage}
    isProfilePage={true}
  />
  <Modal
    on:close={updateUserPage}
    closeButton={CustomCloseButton}
    classWindow="relative w-75 max-w-full max-h-full my-2 mx-auto rounded shadow-md base-forced"
    ><ContentEdit /></Modal
  >
{/if}
