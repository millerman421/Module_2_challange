# Loan Qualifier Application [Module assignment for FinTech Bootcamp]

This is a python command-line interface application that allows users to see qualifying loans from lenders quickly and easily. The application works by taking in a `daily_rate_sheet` of loan criteria from various loan providers, asking the user a number of questions to evaluate their loan eligibility, and then returning to them a list of qualifying loans which is provided saved as `results` or printed to screen.

---

## Technologies

This project leverages python 3.8.8 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [sys](https://docs.python.org/3.8/library/sys.html) - Information about this library.

* [os](https://docs.python.org/3.8/library/os.html) - Information about this library.

* [csv](https://docs.python.org/3.8/library/csv.html) - Information about this library.

* [pathlib](https://docs.python.org/3.8/library/pathlib.html) - Information about this library.
---

## Installation Guide

```python
  pip install fire
  pip install questionary

  The other libraries should be part of the standard Python installation. 
```

---

---

## Usage

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

Upon launching the loan qualifier application you will be greeted with the following prompts.

--------------
###Prompt_01: Borrower provides a file path
![Loan Qualifier Prompts_01](Images/01_Provide_File_Path.PNG)
###Prompt_02: Borrower does not qualify, 0 banks returned
![Loan Qualifier Prompts_02](Images/02_Does_not_qualify.PNG)
###Prompt_03: Bad rate sheet or not in the directory
![Loan Qualifier Prompts_03](Images/03_Bad_rate_sheet_path.PNG)
###Prompt_04: Borrower asks to save the results
![Loan Qualifier Prompts_04](Images/04_Save_Results.PNG)
###Prompt_05: The resuls are saved successfully
![Loan Qualifier Prompts_05](Images/05_Save_Results_Successful.PNG)
###Prompt_06: Borrwer did not want results saved, so they are printed to screen
![Loan Qualifier Prompts_06](Images/06_Print_Results_Successful.PNG)
###Prompt_07: Borrwer provided an invalid directory
![Loan Qualifier Prompts_07](Images/07_Save_Results_Unsuccessful_try_again.PNG)
###Prompt_08: Borrower provided a valid directory after being asked to try again
![Loan Qualifier Prompts_08](Images/08_Save_Results_Unsuccessful_try_again_successful.PNG)

* It is important the borrower furnish accurate information so that the filters provide an optimal list of banks that the borrower may qualify to submit a loan application.
* The five questions are as follows:

--What's your credit score? 
--What's your current amount of monthly debt?
--What's your total monthly income? 
--What's your desired loan amount?
--What's your home value? 

*The output will follow the prompts already presented above. 

###
>This block of code is important to ensure the user gets their output saved correctly. It is a `while` loop that captures the file path
and confirms it is valid. The `while` loop ends once a valid directory is provided and proceeds to call the `save_csv` function to save the details
of the qualifying loans. 

```python
if  save_as_file_answer == True:
        save_file_response = questionary.text("Please provide an output file path for the results.csv file:").ask()
        while not os.path.isdir(save_file_response):
            print("Oops! That file path does not exist. So let's try that again")
            save_file_response = questionary.text("Please provide an output file path again:").ask()
        save_file_response_results = save_file_response + "results.csv"
        save_file_path = Path(save_file_response_results)
        save_csv(qualifying_loans,save_file_path)
```
---

## Contributors

Brian Miller
* ![Contact](mailto:bam4217@yahoo.com)

---

## License

No license required.
