<script context="module" lang="ts">
  export async function fetchURL(url: string, default_img: string) {
    try {
      const response = await fetch(url);
      if (response.ok) {
        return URL.createObjectURL(await response.blob());
      } else {
        return default_img;
      }
    } catch (error) {
      return default_img;
    }
  }

  export async function fetchInfo(url: string) {
    try {
      const response = await fetch(url);
      if (response.ok) {
        return await response.json();
      }
    } catch (error) {
      console.error(error);
    }
  }
</script>
