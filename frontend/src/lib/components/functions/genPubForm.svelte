<script context="module" lang="ts">
  import type { Publication } from "../types/publication.svelte";
  export function genFormData(
    event: any,
    username: string,
    publication: Publication,
  ) {
    const formData = new FormData();
    formData.append("thumbnail", event.target.file.files[0]);
    formData.append("username", username);
    formData.append("title", publication.title);
    formData.append("pub_type", publication.pubType);
    formData.append("short_desc", publication.shortDesc);
    formData.append("long_desc", publication.longDesc);
    formData.append("id", publication.pubID.toString());
    return formData;
  }
</script>
