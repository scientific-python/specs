---
title: "SPEC 3 — Accessibility"
date: 2022-02-14
author:
  - "Juanita Gomez <juanitagomezr2112@gmail.com>"
  - "Sarah Kaiser <sckaiser@sckaiser.com>"
discussion: https://discuss.scientific-python.org/t/spec-3-accessibility/63
endorsed-by:
---

## Description

Technology is a great tool to make the world accessible to the full range of human experience, which includes [those with disabilities](https://www.cdc.gov/ncbddd/disabilityandhealth/infographic-disability-impacts-all.html). The reach of accessibility guidelines extends beyond the scientific Python ecosystem including the [Web Content Accessibility Guidelines (W3C)](https://www.w3.org/TR/WCAG/), a comprehensive set of international standards designed to make web content more accessible.

The primary objective of this SPEC (Scientific Python Accessibility) is to provide fundamental recommendations for the Scientific Python communities and their projects. These recommendations aim to ensure accessibility and inclusivity for individuals with disabilities, particularly regarding web-based content and tools.

As active members of the scientific Python and open-source software (OSS) communities, we are dedicated to leveraging technology to create an inclusive environment that embraces everyone.

It is important to note that accessibility is an ongoing journey, and you need not be overwhelmed by the many recommendations outlined in the provided resources. Taking an incremental approach allows for continuous improvement, ensuring that each enhancement makes technology more accessible and user-friendly.

### Core Project Endorsement

<!--
Briefly discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Briefly discuss what it means for a project to adopt this SPEC.
-->

## Implementation

### 1. Alt text

All images, figures, and media elements on the web should be provided with meaningful [alt text](https://www.w3.org/WAI/test-evaluate/preliminary/#images). Alt text is meant to give screen readers something to read aloud to visually impaired users.

### 2. Color

- **Contrast levels** between content and the background should be enough for anyone with low vision impairments and color deficiencies to be able to read. We list here the recommended values for contrast depending on the size of the text or element on the website. Still, we recommend using an [automated tool](https://hackmd.io/VMHHxV7dR0mwuNuSYci7xw?both) to measure these values for your website.
  - Normal text: [Level AA](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum) compliance requires a contrast ratio of 4.5:1.
  - Large text: Level AA compliance requires a contrast ratio of 3:1.
  - Icons: Level AA compliance requires a contrast ratio of 3.0:1.
- Make sure your website/application is **colorblind friendly**. There are several ways to do this:
  - Convey information in some other way (not using colors).
  - Use [color palettes that are colorblind friendly](https://jfly.uni-koeln.de/color/#pallet), meaning that they avoid certain combinations of colors, and try to maximize the contrast between colors for a variety of common color blind conditions.

### 3. Navigation consistency (tab stops)

Users must be able to interact with a software application using only a keyboard. For this, you should have properly designed [tab stops](https://accessibilityinsights.io/docs/windows/reference/tabstops/). A tab stop is where the cursor stops after the Tab key is pressed.

- Provide a **visible focus** indicator on the interactive element with input focus, usually a border or other visible changes.
- Make all **interactive elements focusable**, allowing users to tab to them unless disabled.
- Maintain a **consistent tab order** that matches the visual hierarchy, including elements that appear in multiple views.

### 4. Mobile friendly

- Implement a **responsive layout** for your website to ensure it adapts well to different screen sizes and devices.
- **Optimize the speed** of your website by minimizing file sizes, leveraging caching, and optimizing images.
- **Avoid using pop-ups** on mobile devices as they can be intrusive and disrupt the user experience.
- Use a **large and readable font size** at least 16 pixels or larger for easy legibility on mobile screens.
- **Simplify your website design**, removing clutter and focusing on essential elements for intuitive mobile navigation.

## Tools and Automation to help

### General tools

- [Accessibility Insights](https://accessibilityinsights.io/): Automated browser-based tool that will check all of the above recommendations.
- [Github Action testing](https://github.com/marketplace/actions/web-accessibility-evaluation) based on A11y recommendations.
- [Axe](https://github.com/dequelabs/axe-core): Open source library (and other paid tooling) that can automate front-end testing.

### Color testing

- [Color blind accessible pallets in Bokeh.](https://docs.bokeh.org/en/latest/docs/reference/palettes.html#large-palettes)
- [Microsoft guide](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/accessibility/test-color-blindness) about color blind checking via browser tools.

## Need more?

While the recommendations provided here cover important aspects of accessibility, they are not comprehensive. It's essential to explore additional resources and practices to further improve accessibility in your website or applications. Here are some additional resources to consider for enhancing accessibility:

- The [Web Content Accessibility Guidelines (W3C)](https://www.w3.org/TR/WCAG/) provide a comprehensive set of international standards for enhancing web content accessibility.
- The [comprehensive checklist](https://www.a11yproject.com/checklist/) published by the A11y organization offers a user-friendly description of the W3C's accessibility standards.
- The [Numfocus Discover Cookbook](https://discover-cookbook.numfocus.org/intro.html) is a valuable resource for understanding event/meeting accessibility and implementing inclusive practices.
- The [Accessibility Insights YouTube channel](https://www.youtube.com/@AccessibilityInsights) provides tutorials on using Accessibility Insights tools to test and improve website accessibility.
- The articles available on the The [axxeslab Articles website](https://axesslab.com/articles/) offer helpful information about accessibility and testing.

## Submit your feedback

We value your feedback and are committed to continuously improving accessibility. If you have any concerns or suggestions regarding accessibility that you believe we may have overlooked, we encourage you to share them with us. Your input is essential to our learning and growth. Please submit your issues and specific accessibility requirements to our [SPECS repository](https://github.com/scientific-python/specs) so that we can address them effectively.
