Feature: Open Registration Page

  @title @form_fill_in
  Scenario: Open Registration Page
    Given I open Gmail registration page
     Then I found the title of Create your Google Account
     Then I fill the Gamil Registration form
     Then I clicked on Submit button to continue

  @drop-down
  Scenario: Drop-down value selection
     Then I select dropdown items from the-internet.herokuapp.com/dropdown

  @checkbox
  Scenario: Checkbox value selection
     Then I select checkbox items from the-internet.herokuapp.com/checkboxes

  @radio_button
  Scenario: Radio Button selection
     Given I select checkbox items from seleniumframework.com/Practiceform

  @select_date
  Scenario: Date Selection
     Given I select Date from calender at seleniumframework.com/Practiceform