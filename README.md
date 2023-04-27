# romanos

Vamos a jugar con los números romanos y Python

## Cómo se convierte un número natural menor que 4000 a Romano

```
  1123 ==> MCXXIII
  ||||________III ------- 3 * 10⁰ = 3*1 = 3 ======== III
  |||_______ XX --------- 2 * 10¹ = 2*10 = 20 ====== XX
  ||_______ C ----------- 1 * 10² = 1*100 = 100 ==== C
  |_______ M ------------ 1 * 10³ = 1*1000 = 1000 == M
```

  Descompongo el número en millares, centenas, decenas, unidades
  1
  1
  2
  3

## Cómo se convierte un número romano a entero

```
  MCXXIII ==> 1123

  1000 + 100 + 10 + 10 + 1 + 1 + 1


  CM ==> 900
  MC ==> 1100
  MIX ==> 1000 1 10 --- 1000 + 10 - 1

```
