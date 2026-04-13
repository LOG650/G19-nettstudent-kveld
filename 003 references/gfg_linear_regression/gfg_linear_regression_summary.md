# Linear Regression in Machine Learning – Sammendrag

## APA 7-referanse

GeeksforGeeks. (2026, 6. april). *Linear Regression in Machine Learning*. Hentet 13. april 2026 fra https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/

## Metadata

- **Hentet dato:** 13. april 2026
- **Opprinnelig publisert:** 6. april 2026
- **Forfatter(e):** GeeksforGeeks
- **URL:** https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/

---

## Sammendrag

**Linear Regression** er en fundamental supervíst læringsalgoritme som modellerer forholdet mellom en avhengig variabel (target) og en eller flere uavhengige variabler (prediktorer). Algoritmen predikerer kontinuerlige verdier ved å tilpasse en rett linje som best representerer dataene.

### Grunnleggende konsepter

Linear regression er basert på å finne den beste tilpassede linjen som minimerer feilen (differansen) mellom observerte datapunkter og predikerte verdier. I den enkleste form (simpel lineær regresjon) er ligningen:

$$y = \theta_0 + \theta_1 x$$

Hvor:
- $y$ er den predikerte verdien (avhengig variabel)
- $x$ er inngangen (uavhengig variabel)
- $\theta_0$ er interceptet (verdien av $y$ når $x = 0$)
- $\theta_1$ er stigningstallet (hvor mye $y$ endres når $x$ endres med en enhet)

### Minste kvadraters metode

For å finne den beste tilpassede linjen brukes **Least Squares**-metoden, som minimerer summen av kvadrerte differanser mellom faktiske og predikerte verdier (residualer):

$$\text{Residual} = y_i - \hat{y}_i$$

$$\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 \rightarrow \text{minimere}$$

### Typer av lineær regresjon

1. **Simpel lineær regresjon:** Bruker én uavhengig variabel. Eksempel: predikering av eksamensscore basert på timer studert.

2. **Multipel lineær regresjon:** Bruker flere uavhengige variabler:
   $$\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_n x_n$$

### Kritiske antagelser

Linear regression forutsetter:
- **Linearitet:** Relasjon mellom variablene er lineær
- **Uavhengighet av feil:** Prediksjonfeil påvirker ikke hverandre
- **Homoskedastisitet:** Feilen har lik varians over alle inputverdier
- **Normalitet:** Feilen følger normalfordeling
- **Ingen multikollinearitet:** Inputvariabler er ikke sterkt korrelerte

### Optimaliseringsmetoder

**Kostfunksjon (Mean Squared Error):**
$$J = \frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2$$

**Gradient Descent** brukes for iterativt å oppdatere parametrene og minimisere kostfunksjonen.

### Evalueringsmetrikker

- **RMSE (Root Mean Squared Error):** Kvadratroten av gjennomsnittlig kvadrert feil
- **R² (R-squared):** Hvor stor andel av variansen som er forklart (0–1)
- **MAE (Mean Absolute Error):** Gjennomsnittlig absolutt avvik
- **Adjusted R²:** R² justert for antall prediktorer

### Fordeler

- Enkelt å implementere og tolke
- Svært effektivt beregningskostnadsvis
- God utgangspunkt-modell for sammenligninger
- Gir innsikt i variabelforhold

### Begrensninger

- Antar lineær relasjon (fungerer dårlig ved komplekse, ikke-lineære forhold)
- Sensitiv for multikollinearitet
- Kan overanpasset eller underanpasset avhengig av data
- Krever god features engineering

---

## Stikkord / Keywords

- Supervised learning
- Regression
- Best-fit line
- Least squares method
- Gradient descent
- Cost function (MSE)
- Simple linear regression
- Multiple linear regression
- R-squared
- Feature engineering
- Overfitting
- Underfitting
