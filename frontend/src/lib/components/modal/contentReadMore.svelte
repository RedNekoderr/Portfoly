<script lang="ts">
  import type { Context } from "svelte-simple-modal";
  import { getContext } from "svelte";
  import PopupReadMore from "./popupReadMore.svelte";
  import type { Publication } from "../types/publication.svelte";

  export let publication: Publication;

  const { open } = getContext<Context>("simple-modal");
  const Show = () =>
    open(PopupReadMore, {
      title: publication.title,
      longDesc: publication.longDesc,
    });
</script>

<button on:click={Show} class="btn btn-primary btn-sm">Read More</button>
