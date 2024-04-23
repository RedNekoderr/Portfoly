<script context="module" lang="ts">
  export interface Publication {
    pubID: number;
    date: string;
    title: string;
    pubType: string;
    shortDesc: string;
    longDesc: string;
    blob: string;
    username: string;
    avatar: string;
  }

  export function createPublication(
    pubID: number,
    date: string,
    title: string,
    pubType: string,
    shortDesc: string,
    longDesc: string,
    blob: string,
    username: string = "",
    avatar: string = "",
  ): Publication {
    let publication: Publication = {
      pubID: pubID,
      date: date,
      title: title,
      pubType: pubType,
      shortDesc: shortDesc,
      longDesc: longDesc,
      blob: blob,
      username: username,
      avatar: avatar,
    };
    return publication;
  }
</script>
