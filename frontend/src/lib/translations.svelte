<script context="module" lang="ts">
  export interface Translations {
    [locale: string]: {
      [key: string]: string;
    };
  }

  const translations: Translations = {
    en: {
      "home.title": "Showcase your portfolio",
      "home.title.subtitle": "Portfolio sharing platform",
      "home.title.button.getStarted": "Get Started",
      "home.title.button.learnMore": "Learn More",
      "home.features.title": "Our features",
    },
    ru: {
      "home.title": "Поделитесь своим портфолио",
      "home.title.subtitle": "Платформа для хранения и показа портфолио",
      "home.title.button.getStarted": "Приступим",
      "home.title.button.learnMore": "Узнать больше",
      "home.features.title": "Наши возможности",
    },
  };

  export { translations };
</script>
