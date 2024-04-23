<script context="module" lang="ts">
  import { derived, writable } from "svelte/store";
  import { translations } from "./translations.svelte";
  import type { Writable } from "svelte/store";

  export const locale: Writable<string> = writable("en");
  export const locales: string[] = Object.keys(translations);

  function translate(
    locale: string,
    key: string,
    vars: Record<string, string>,
  ): string {
    if (!key) throw new Error("no key provided to $t()");
    if (!locale) throw new Error(`no translation for key "${key}"`);

    let text: string = translations[locale][key];

    if (!text) throw new Error(`no translation found for ${locale}.${key}`);

    Object.keys(vars).map((k) => {
      const regex = new RegExp(`{{${k}}}`, "g");
      text = text.replace(regex, vars[k]);
    });

    return text;
  }

  export const t = derived(
    locale,
    ($locale) =>
      (key: string, vars: Record<string, string> = {}): string =>
        translate($locale, key, vars),
  );
</script>
