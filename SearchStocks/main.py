from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from json import load
from re import findall
from time import sleep

class SearchStocks:
    def __init__(self, script_file: str):
        """
        initialize a firefox browser driver hiding the GUI, and start the script file in json format

        args:
            script_file: str → name of the script file (e.g., `Script.json`)

        output:
            None

        time complexity → o(1)
        """
        options = Options()
        options.add_argument("--headless")

        self.driver = webdriver.Firefox(options=options)

        # open a script file in reading mode and load to json (`dict` format)
        with open(script_file, 'r', encoding="utf-8") as sf:
            self.script = load(sf)

    def interface(self):
        """
        manage all the logic of the command-interface for `SearchStocks`

        args:
            None

        output:
            None

        time complexity → o(n)
        """
        print(self.script['greeting'])
        
        while True:
            query = input("\nType the name of your stock (or `exit`): ")

            # checks if the user wants to exit and close the quit the driver
            if query == 'exit':
                self.driver.quit()
                break

            sanitized_query = self._sanitize(query)
            stocks_dict = self._find_stocks(f'{sanitized_query}+stocks')

            # confirm if there was an exception
            if stocks_dict.get('exception'):
                print(stocks_dict['exception'])

            else:
                response_template = self.script['response']
                response = response_template.format(**stocks_dict) # replace the template with the stock information

                print(f"\n{response}")

    def _sanitize(self, query: str):
        """
        clean with regular expresion all the characters and turn to lowercases

        args:
            query: str → raw query (e.g., m$i03c@#3ros%^&*f%7t!)

        output:
            str → sanitized in a-z and lower characters

        time compleity → o(n)
        """
        return ''.join(findall('[a-z]', query.lower()))

    def _get(self, query: str):
        """
        use a firefox driver and create a query to the duckduckgo website

        args:
            query: str → sanitized and prepared search query 

        output:
            WebDriver → browser object with a website open

        time complexity → o(1)
        """
        self.driver.get(f"https://duckduckgo.com/?q={query}/")
        self._visual_loader(0.66)

        return self.driver
    
    def _find_stocks(self, query):
        """
        fetch a get method with a query, and save the stock in a dict

        args:
            query: str → browser object with a website open

        output:
            stocks_dict: dict(str) → dict with title, price and currency for the stock
            exception: dict → log error for `NoSuchElement` and other exceptions

        time complexity → o(n)
        """
        driver = self._get(query)

        try:
            # search each element with labels in string format
            stocks_dict = {
                    "title": driver.find_element(By.CSS_SELECTOR, ".module__title").text,
                    "price": driver.find_element(By.CSS_SELECTOR, ".stocks-module__currentPrice").text,
                    "currency": driver.find_element(By.CSS_SELECTOR, ".stocks-module__currency").text
                }
            
            return stocks_dict
        
        except NoSuchElementException:
            return {"exception": "\nSorry, we have an error. Try with other stock (e.g., microsoft)."}

        except Exception as e:
            return {"exception": f"\nAn error has been ocurred: {str(e)[:17]}..."}

    def _visual_loader(self, time_per_step: float):
        """
        create a command-line loader with points and defining the time per step

        args:
            time_per_step: float → seconds per step (e.g., 0.45, 1.34,...)

        output:
            None

        time complexity → o(1)
        """
        print("Loading", end='', flush=True)
        for _ in range(3):
            # whait the time per step, and add points in the same line
            sleep(time_per_step), print('.', end='', flush=True)
            
        print()

if __name__ == "__main__":
    stocks = SearchStocks('script.json')
    stocks.interface()
