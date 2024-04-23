<script context="module" lang="ts">
  import { fetchURL } from "./fetch-info.svelte";
  import { createPublication } from "../types/publication.svelte";
  import { fetchInfo } from "./fetch-info.svelte";
  import type { Publication } from "../types/publication.svelte";

  const fetch_url = "http://localhost:5000/api/get-info/";

  function transformDateString(dateString: string): string {
    const date = new Date(dateString);

    const transformedString = date.toLocaleDateString("en-US", {
      day: "numeric",
      month: "short",
      year: "numeric",
    });

    return transformedString;
  }

  async function fetchPublication(username: string) {
    let publications = await fetchInfo(
      `${fetch_url}user/publications?username=${username}`,
    );

    if (publications) {
      for (let i = 0; i < publications.publications.length; i++) {
        let urlBlob = await fetchURL(
          `${fetch_url}publication-thumbnail?id=${publications.publications[i].id}`,
          "images/default-thumbnail.png",
        );
        Object.assign(publications.publications[i], { blob: urlBlob });
      }
      return publications.publications;
    }
  }

  async function createPublicationList(username: string) {
    let publications: Publication[] = [];
    for (let publication of await fetchPublication(username)) {
      publications.push(
        createPublication(
          publication.id,
          transformDateString(publication.date),
          publication.title,
          publication.pub_type,
          publication.short_desc,
          publication.desc,
          publication.blob,
        ),
      );
    }
    return publications;
  }

  export const getPublications = async (username: string) => {
    return await createPublicationList(username);
  };
</script>
