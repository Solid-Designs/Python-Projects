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
    
    // Get the total budget amount, subtract it from the current MTD spend, then divide by the amount of days left in the current month
    function getDailyBudget(totalBudget) {
      var dailyBudget = Math.round((totalBudget - getMonthlySpend()) / getDaysInMonth());
      console.log("The daily budget should be: $", dailyBudget);
      return dailyBudget;
    }
    
    // Iterate through the campaigns and split the budget evenly
    function setDailyBudget(){
      var campaignSelector = AdsApp.campaigns().withCondition("campaign.status = ENABLED");
      var campaignIterator = campaignSelector.get();
      var budgetSelector = AdsApp.budgets().withCondition("campaign.status = ENABLED");
      var budgetIterator = budgetSelector.get();
  
      while (campaignIterator.hasNext()) { // Campaign iterator
        var campaign = campaignIterator.next();
        console.log(campaign.getName());
        console.log(campaign.getBudget().getAmount());
        campaign.getBudget().setAmount(getDailyBudget(2000));    // <----------------------- UPDATE TOTAL BUDGET HERE!
      }
    }
    
    // Function calls here:
    setDailyBudget();
  }