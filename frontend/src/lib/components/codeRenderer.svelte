<script lang="ts">
  import Highlight from "svelte-highlight";
  import github from "svelte-highlight/styles/github";
  import { matchLanguageModule } from "./functions/matchLangModule.svelte";
  import { onMount } from "svelte";
  export let text: string;
  export let lang: string;
  let languageModule: any;
  onMount(async () => {
    languageModule = await matchLanguageModule(lang);
  });
</script>

<svelte:head>
  {@html github}
</svelte:head>

{#if languageModule}
  <Highlight language={languageModule} code={text} />
{/if}
