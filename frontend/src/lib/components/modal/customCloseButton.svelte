<!-- CloseButton.svelte -->
<script lang="ts">
  // This property is used by Modal.svelte to pass down the close function
  export let onClose: any;
  import { XLg } from "svelte-bootstrap-icons";
</script>

<div class="buttons">
  <button on:click={onClose} type="button" class="close" aria-label="Close"
    ><XLg /></button
  >
  <!-- <button on:click={onExpand} type="button" class="expand" aria-label="Close"
    ><ChevronExpand /></button
  > -->
</div>

<style lang="scss">
  * {
    padding: 0;
    margin: 0;
  }

  button {
    border: none;
    border-radius: 50%;
    padding: 0 0.25rem;
    transition: all 0.2s ease-in-out;
    margin-right: 0.5rem;
  }

  .buttons {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    position: absolute;
    z-index: 10;
    top: 0.55rem;
    left: 1rem;
  }

  button:hover {
    filter: brightness(0.9);
    color: var(--base);
  }

  .close {
    background: var(--rose);
    color: var(--rose);
  }

  //.expand {
  //  background: var(--pine);
  //  color: var(--pine);
  //}
</style>
