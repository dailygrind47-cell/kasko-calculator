import tkinter as tk
from tkinter import ttk, messagebox
import sys

class KASKOCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор КАСКО")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Стили
        style = ttk.Style()
        style.theme_use('clam')
        
        # Основной фрейм
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Заголовок
        title_label = ttk.Label(main_frame, text="Калькулятор стоимости КАСКО", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Параметры автомобиля
        ttk.Label(main_frame, text="=== Параметры автомобиля ===", 
                  font=('Arial', 11, 'bold')).grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        ttk.Label(main_frame, text="Стоимость авто (руб):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.car_price = ttk.Entry(main_frame, width=30)
        self.car_price.insert(0, "2500000")
        self.car_price.grid(row=2, column=1, pady=5)
        
        ttk.Label(main_frame, text="Возраст авто (лет):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.car_age = ttk.Combobox(main_frame, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], width=27)
        self.car_age.set(3)
        self.car_age.grid(row=3, column=1, pady=5)
        
        # Параметры водителя
        ttk.Label(main_frame, text="=== Параметры водителя ===", 
                  font=('Arial', 11, 'bold')).grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))
        
        ttk.Label(main_frame, text="Возраст водителя:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.driver_age = ttk.Entry(main_frame, width=30)
        self.driver_age.insert(0, "35")
        self.driver_age.grid(row=5, column=1, pady=5)
        
        ttk.Label(main_frame, text="Стаж вождения (лет):").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.driver_exp = ttk.Entry(main_frame, width=30)
        self.driver_exp.insert(0, "10")
        self.driver_exp.grid(row=6, column=1, pady=5)
        
        # Дополнительные параметры
        ttk.Label(main_frame, text="=== Дополнительные параметры ===", 
                  font=('Arial', 11, 'bold')).grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))
        
        ttk.Label(main_frame, text="Регион:").grid(row=8, column=0, sticky=tk.W, pady=5)
        self.region = ttk.Combobox(main_frame, 
                                   values=["Москва/СПб (1.25)", "Крупный город (1.1)", "Регион (1.0)"], 
                                   width=27)
        self.region.set("Москва/СПб (1.25)")
        self.region.grid(row=8, column=1, pady=5)
        
        ttk.Label(main_frame, text="Франшиза (руб):").grid(row=9, column=0, sticky=tk.W, pady=5)
        self.franchise = ttk.Combobox(main_frame, 
                                      values=["0", "15000", "30000", "50000"], 
                                      width=27)
        self.franchise.set("0")
        self.franchise.grid(row=9, column=1, pady=5)
        
        ttk.Label(main_frame, text="Ремонт:").grid(row=10, column=0, sticky=tk.W, pady=5)
        self.repair_type = ttk.Combobox(main_frame, 
                                        values=["У дилера", "На СТОА"], 
                                        width=27)
        self.repair_type.set("У дилера")
        self.repair_type.grid(row=10, column=1, pady=5)
        
        ttk.Label(main_frame, text="Тип покрытия:").grid(row=11, column=0, sticky=tk.W, pady=5)
        self.coverage = ttk.Combobox(main_frame, 
                                     values=["Полное КАСКО", "Только ущерб", "Угон + Тотал"], 
                                     width=27)
        self.coverage.set("Полное КАСКО")
        self.coverage.grid(row=11, column=1, pady=5)
        
        # Кнопка расчета
        calc_button = ttk.Button(main_frame, text="РАССЧИТАТЬ СТОИМОСТЬ", 
                                 command=self.calculate, style='Accent.TButton')
        calc_button.grid(row=12, column=0, columnspan=2, pady=30, sticky=(tk.W, tk.E))
        
        # Результат
        self.result_frame = ttk.LabelFrame(main_frame, text="Результат расчета", padding="15")
        self.result_frame.grid(row=13, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.result_text = tk.Text(self.result_frame, height=10, width=60, 
                                   font=('Consolas', 10), state=tk.DISABLED)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
    def calculate(self):
        try:
            # Получение данных
            car_price = int(self.car_price.get())
            car_age = int(self.car_age.get())
            driver_age = int(self.driver_age.get())
            driver_exp = int(self.driver_exp.get())
            
            # Парсинг региона
            region_text = self.region.get()
            if "Москва" in region_text:
                region_risk = 1.25
            elif "Крупный" in region_text:
                region_risk = 1.1
            else:
                region_risk = 1.0
            
            franchise = int(self.franchise.get())
            repair_at_dealer = "дилера" in self.repair_type.get()
            
            coverage_text = self.coverage.get()
            if "Полное" in coverage_text:
                coverage_type = "full"
            elif "ущерб" in coverage_text:
                coverage_type = "constructive"
            else:
                coverage_type = "total_only"
            
            # Расчет
            calc = KASKOCalculator(
                car_price=car_price,
                car_age_years=car_age,
                driver_age=driver_age,
                driver_experience_years=driver_exp,
                region_risk=region_risk,
                franchise=franchise,
                repair_at_dealer=repair_at_dealer,
                coverage_type=coverage_type
            )
            
            result = calc.calculate()
            
            # Форматирование результата
            result_str = f"""
Базовая стоимость: {result['base_price']:,.0f} руб.
Итоговый коэффициент: {result['total_coefficient']}

Детализация коэффициентов:
  • Возраст авто: {result['breakdown']['Возраст авто']}
  • Водитель: {result['breakdown']['Водитель']}
  • Франшиза: {result['breakdown']['Франшиза']}
  • Тип ремонта: {result['breakdown']['Тип ремонта']}
  • Покрытие: {result['breakdown']['Покрытие']}
  • Регион: {result['breakdown']['Регион']}

═══════════════════════════════════
ИТОГО К ОПЛАТЕ: {result['final_price']:,.0f} руб.
═══════════════════════════════════
"""
            
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)
            self.result_text.config(state=tk.DISABLED)
            
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


class KASKOCalculator:
    def __init__(self, car_price, car_age_years, driver_age, driver_experience_years, 
                 region_risk=1.0, franchise=0, repair_at_dealer=True, coverage_type="full"):
        self.car_price = car_price
        self.car_age = car_age_years
        self.driver_age = driver_age
        self.driver_exp = driver_experience_years
        self.region_risk = region_risk
        self.franchise = franchise
        self.repair_at_dealer = repair_at_dealer
        self.coverage_type = coverage_type

    def _get_base_rate(self):
        return 0.025

    def _get_car_age_coeff(self):
        if self.car_age <= 1: return 1.0
        elif self.car_age <= 3: return 1.05
        elif self.car_age <= 5: return 1.2
        elif self.car_age <= 7: return 1.4
        else: return 1.7

    def _get_driver_coeff(self):
        if self.driver_age < 25 or self.driver_exp < 3:
            return 1.4
        elif self.driver_age < 30 or self.driver_exp < 5:
            return 1.1
        else:
            return 0.9

    def _get_franchise_coeff(self):
        if self.franchise == 0: return 1.0
        elif self.franchise <= 15000: return 0.85
        elif self.franchise <= 30000: return 0.75
        else: return 0.60

    def _get_repair_coeff(self):
        return 1.25 if self.repair_at_dealer else 1.0

    def _get_coverage_coeff(self):
        if self.coverage_type == "full": return 1.0
        elif self.coverage_type == "constructive": return 0.65
        elif self.coverage_type == "total_only": return 0.40
        return 1.0

    def calculate(self):
        base_rate = self._get_base_rate()
        
        K_car = self._get_car_age_coeff()
        K_driver = self._get_driver_coeff()
        K_franchise = self._get_franchise_coeff()
        K_repair = self._get_repair_coeff()
        K_coverage = self._get_coverage_coeff()
        K_region = self.region_risk

        total_coeff = K_car * K_driver * K_franchise * K_repair * K_coverage * K_region
        final_price = self.car_price * base_rate * total_coeff

        return {
            "base_price": self.car_price * base_rate,
            "total_coefficient": round(total_coeff, 2),
            "final_price": round(final_price, -1),
            "breakdown": {
                "Возраст авто": K_car,
                "Водитель": K_driver,
                "Франшиза": K_franchise,
                "Тип ремонта": K_repair,
                "Покрытие": K_coverage,
                "Регион": K_region
            }
        }


if __name__ == "__main__":
    root = tk.Tk()
    app = KASKOCalculatorGUI(root)
    root.mainloop()