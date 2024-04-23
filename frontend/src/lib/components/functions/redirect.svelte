<script context="module" lang="ts">
  import { goto } from "$app/navigation";
  import { browser } from "$app/environment";
  export async function redirect(link: string) {
    if (browser) {
      goto(link);
      return;
    }
  }
</script>
