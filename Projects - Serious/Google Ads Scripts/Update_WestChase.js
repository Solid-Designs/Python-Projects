function main() {
    function getDaysInMonth() {
    var currentTime = new Date(); // Get the current time
    var today = currentTime.getDate(); // Get the current day
    var month = currentTime.getMonth(); // Get the current month
    var daysLeft = setDaysInMonth(month + 1, currentTime.getFullYear()) - today; // Add 1 to the month to get the end of the current month
    console.log("There are: ", daysLeft , "days left this month" )
    return daysLeft;
  }
  
  // Input the current year, then the current month, then 0 as the day to get the last day of the previous month
  function setDaysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
  }
  
  // Get the MTD cost **NOTE: This will need to be updated because there is only one campaign here**
  function getMonthlySpend() {
    var campaignSelector = AdsApp.campaigns().withCondition("campaign.status = ENABLED");
    var campaignIterator = campaignSelector.get();
    
    var sum = 0;
    
    while (campaignIterator.hasNext()) {
      var campaign = campaignIterator.next();
      var stats = campaign.getStatsFor("THIS_MONTH");
      var cost = Math.round(stats.getCost());
      var total = sum += cost;
    }
    
    console.log("You have spent: $", total, "this month");
    return total;
  }
  

function updateBudgets() {
  var sheet = SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/10g7qmYjH7BSX7kHKktr_ZTaXdgIyuUlJ-cPA0YHT0J4/edit?usp=sharing').getSheetByName('Sheet1');
  var data = sheet.getDataRange().getValues();
  var budget = data[1][2];
  
  // Get the total budget amount, subtract it from the current MTD spend, then divide by the amount of days left in the current month
  var dailyBudget = Math.round((parseFloat(budget) - getMonthlySpend()) / getDaysInMonth());
  console.log(dailyBudget);

  // Loop through the rows in the sheet and update the budgets for the specified campaigns
  for (var i = 1; i < data.length; i++) {
      // Row 1 is the header row, so we skip it
      // Row 2 is the first row of data and it is the campaign name
      // Column 1 is the second row of data and it is the budget
      var campaignName = data[i][0];
      var percentage = data[i][1];
      
      console.log("The budget should be: ", Math.round(dailyBudget * (percentage/100)));
    
      // Get the campaign name from the sheet and update the budget
    
      var campaignIterator = AdsApp.campaigns()
          .withCondition("Name = '" + campaignName + "'")
          .get();
      if (campaignIterator.hasNext()) {
          var campaign = campaignIterator.next();
          campaign.getBudget().setAmount(Math.round(dailyBudget * (percentage/100)));
      }
  }
}
updateBudgets();
}