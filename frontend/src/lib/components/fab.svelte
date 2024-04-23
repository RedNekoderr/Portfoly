<script lang="ts">
  import { PencilSquare } from "svelte-bootstrap-icons";
  export let func: () => void;
</script>

<div class="fab-container">
  <div class="fab-content">
    <button class="button p-3 m-0" on:click={func}
      ><PencilSquare width={24} height={24} /></button
    >
  </div>
</div>

<style lang="scss">
  .fab-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
    user-select: none;
    position: fixed;
    bottom: 30px;
    right: 30px;
  }

  button {
    background-color: var(--foam);
    border-radius: 50%;
  }
</style>
