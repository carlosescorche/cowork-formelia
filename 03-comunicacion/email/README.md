# Email

Copys y secuencias de email. El envío transaccional vive en el producto (Resend); aquí se
redactan, versionan y auditan los textos antes de llevarlos al código, y se gestiona la
newsletter.

## Estructura

```
email/
├── ciclo-de-vida/     Secuencias de onboarding/activación (un .md por email, con asunto,
│                      preview text, cuerpo y CTA)
├── newsletter/        Ediciones de la newsletter quincenal: AAAA-MM-DD-slug.md
└── plantillas/        Plantillas reutilizables (anuncio de feature, incidente, hito)
```

## Convenciones

- Cada email: frontmatter con `asunto`, `preview`, `disparador` (evento que lo envía),
  `objetivo` (la acción que buscamos) y `estado`.
- Asunto ≤45 caracteres, en español, sin mayúsculas de grito ni emojis por defecto.
- Remitente: nombre humano ("Carlos de Formelia").
- Un CTA por email.

## Auditoría pendiente del ciclo de vida actual (del producto)

- [ ] Asunto del email de confirmación está en inglés → corregir en producto.
- [ ] Revisar toda la secuencia de onboarding contra [voz-y-tono](../../01-marca/voz-y-tono.md).
- [ ] Verificar que el digest diario tenga opt-out claro y honesto.
