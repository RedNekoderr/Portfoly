<script context="module" lang="ts">
  import { python } from "svelte-highlight/languages/python";
  import { java } from "svelte-highlight/languages/java";
  import { javascript } from "svelte-highlight/languages/javascript";
  import { c } from "svelte-highlight/languages/c";
  import { cpp } from "svelte-highlight/languages/cpp";
  import { csharp } from "svelte-highlight/languages/csharp";
  import { php } from "svelte-highlight/languages/php";
  import { typescript } from "svelte-highlight/languages/typescript";
  import { rust } from "svelte-highlight/languages/rust";
  import { go } from "svelte-highlight/languages/go";
  import { lua } from "svelte-highlight/languages/lua";

  export const matchLanguageModule = async (lang: string) => {
    switch (lang.toLowerCase()) {
      case "python":
        return python;
      case "java":
        return java;
      case "javascript" || "js":
        return javascript;
      case "c":
        return c;
      case "cpp" || "c++" || "cxx":
        return cpp;
      case "csharp" || "c#":
        return csharp;
      case "php":
        return php;
      case "typescript" || "ts":
        return typescript;
      case "rust":
        return rust;
      case "go":
        return go;
      case "lua":
        return lua;
    }
  };
</script>
