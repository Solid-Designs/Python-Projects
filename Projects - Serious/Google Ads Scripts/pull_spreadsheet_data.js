function main() {
    function getCampaignNames() {
        // Get the campaigns from Google ads
        var campaigns = AdsApp.campaigns().withCondition("Status = ENABLED").get();
        // Create an array to store the campaign names
        var campaignNames = [];
        // Loop through the campaigns and push the names to the array
        while (campaigns.hasNext()) {
            var campaign = campaigns.next();
            campaignNames.push(campaign.getName());
        }
        // Return the array
        return campaignNames;
    }
    
      function writeCampaignNamesToSheet() {
          var sheetUrl = 'https://docs.google.com/spreadsheets/d/10g7qmYjH7BSX7kHKktr_ZTaXdgIyuUlJ-cPA0YHT0J4/edit?usp=sharing';
          var sheet = SpreadsheetApp.openByUrl(sheetUrl).getSheetByName('Sheet1');
          var campaignNames = getCampaignNames();
    
          for (var i = 0; i < campaignNames.length; i++) {
            // It's getRange(i + 2, 1) to make sure that I am not overwriting the header row
              sheet.getRange(i + 2, 1).setValue(campaignNames[i]);
          }
      }
    
    writeCampaignNamesToSheet();
  }