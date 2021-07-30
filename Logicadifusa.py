import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
# * food quality and service on subjective ranges, 0 to 10
# * tip has a range of 0 to 25 in units of percentage points
x_temperatura = np.arange(35,40,1)
x_aire = np.arange(50,150,1)
x_ultrasonico = np.arange(50,150,1)
x_buzzer = np.arange(1,10,1)
x_filtro = np.arange(1,10,1)

# Generate fuzzy membership functions
temperatura_lo = fuzz.trimf(x_temperatura, [35,35,37])
temperatura_md = fuzz.trimf(x_temperatura, [35,37,39])
temperatura_hi = fuzz.trimf(x_temperatura, [37,39,39])

aire_lo = fuzz.trimf(x_aire, [50,50,100])
aire_md = fuzz.trimf(x_aire, [50,100,150])
aire_hi = fuzz.trimf(x_aire, [100,150,150])

ultrasonico_lo = fuzz.trimf(x_ultrasonico, [50,50,100])
ultrasonico_md = fuzz.trimf(x_ultrasonico, [50,100,150])
ultrasonico_hi = fuzz.trimf(x_ultrasonico, [100,150,150])

buzzer_lo = fuzz.trimf(x_buzzer, [1,1,5])
buzzer_md = fuzz.trimf(x_buzzer, [1,5,10])
buzzer_hi = fuzz.trimf(x_buzzer, [5,10,10])

filtro_lo = fuzz.trimf(x_filtro, [1,1,5])
filtro_md = fuzz.trimf(x_filtro, [1,5,10])
filtro_hi = fuzz.trimf(x_filtro, [5,10,10])
# Visualize the membership functions
fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(7, 8))
ax0.plot(x_temperatura, temperatura_lo, 'b', linewidth=1.5, label='Bajo')
ax0.plot(x_temperatura, temperatura_md, 'g', linewidth=1.5, label='Seguro')
ax0.plot(x_temperatura, temperatura_hi, 'r', linewidth=1.5, label='Peligroso')
ax0.set_title('Temperatura')
ax0.legend()

ax1.plot(x_aire, aire_lo, 'b', linewidth=1.5, label='Buena')
ax1.plot(x_aire, aire_md, 'g', linewidth=1.5, label='Moderada')
ax1.plot(x_aire, aire_hi, 'r', linewidth=1.5, label='Mala')
ax1.set_title('Calidad de aire')
ax1.legend()
ax2.plot(x_ultrasonico, ultrasonico_lo, 'b', linewidth=1.5, label='Seguro')
ax2.plot(x_ultrasonico, ultrasonico_md, 'g', linewidth=1.5, label='Regular')
ax2.plot(x_ultrasonico, ultrasonico_hi, 'r', linewidth=1.5, label='Peligroso')
ax2.set_title('Ultrasonico')
ax2.legend()

ax3.plot(x_buzzer, buzzer_lo, 'b', linewidth=1.5, label='Bajo ruido')
ax3.plot(x_buzzer, buzzer_md, 'g', linewidth=1.5, label='Ruido medio')
ax3.plot(x_buzzer, buzzer_hi, 'r', linewidth=1.5, label='Alto ruido')
ax3.set_title('Buzzer')
ax3.legend()

ax4.plot(x_filtro, filtro_lo, 'b', linewidth=1.5, label='Bajo aire')
ax4.plot(x_filtro, filtro_md, 'g', linewidth=1.5, label='Aire medio')
ax4.plot(x_filtro, filtro_hi, 'r', linewidth=1.5, label='Alto aire')
ax4.set_title('Filtro tipo ventilador')
ax4.legend()



# Turn off top/right axes
for ax in (ax0, ax1, ax2, ax3, ax4):
 ax.spines['top'].set_visible(False)
 ax.spines['right'].set_visible(False)
 ax.get_xaxis().tick_bottom()
 ax.get_yaxis().tick_left()
 
plt.tight_layout()
plt.show()