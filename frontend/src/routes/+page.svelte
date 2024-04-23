<script lang="ts">
  import { onMount } from "svelte";
  import { redirect } from "$lib/components/functions/redirect.svelte";
  import { locale } from "$lib/translate.svelte";
  import {
    getCookie,
    setCookie,
  } from "$lib/components/functions/cookies.svelte";

  function setLocale() {
    const lang = getCookie("locale");
    if (!lang) {
      locale.set("en");
      setCookie("locale", "en", 30, false);
    } else {
      locale.set(lang);
    }
  }

  onMount(() => {
    setLocale();
    redirect("home");
  });
</script>

<section
  class="text title text-center vh-100 d-flex align-items-center justify-content-center"
>
  <p>loading...</p>
</section>
