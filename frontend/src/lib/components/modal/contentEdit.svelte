<script lang="ts">
  import type { Context } from "svelte-simple-modal";
  import { getContext } from "svelte";
  import PopupEdit from "./popupEdit.svelte";
  import Fab from "../fab.svelte";

  const { open } = getContext<Context>("simple-modal");
  const Show = () => open(PopupEdit);
</script>

<Fab func={Show} />
