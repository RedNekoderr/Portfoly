<script context="module" lang="ts">
  import { writable } from "svelte/store";
  import type { Writable } from "svelte/store";
  export const isContentChanged: Writable<boolean> = writable(false);
</script>
