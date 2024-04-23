<script lang="ts">
  import SvelteMarkdown from "svelte-markdown";
  import { marked } from "marked";
  import CodeRenderer from "../codeRenderer.svelte";

  export let title: string = "";
  export let longDesc: string = "";

  const tokens = marked.lexer(longDesc);
</script>

<div class="container h-100">
  <div class="row px-3">
    <h1 class="text title">{title}</h1>
  </div>

  <div class="px-3 text-start">
    <div class="text h2 px-4">Description</div>
    <div class="text-start mt-3 overflow-auto markdown-body">
      <SvelteMarkdown source={tokens} renderers={{ code: CodeRenderer }} />
    </div>
  </div>
</div>

<style>
  h1 {
    font-size: 2em;
  }

  .markdown-body {
    max-height: 65vh;
  }
</style>
