// Pseudocode: Automate numbers requests
// 1. Fill out google form *Done
// 2. Pull data from form *Done
// 3. Place variables in sheets template (Create numbers request template) *Done
// 4. Get the correct AM email (Create radio button question on the form)
// 5. Send to AM via email automatically (Trigger in sheets when a new numbers request is created ) *Done

// TO-DO's:
// Add all 50 states alphabetically *Done
// Take the client's name and place it at the top of the numbers request *Done
// Make the ecommerce section work 
// Make it easier to input percentages (Automatically do a conversion if the number is a whole number) 
// Make it so that when you select a name it will automatically go to the correct email
// Get the industry averages for CPC's, conversion rates, average order values, clv's and close rates
// Create database(spreadsheet) of keywords for each sub-industry to then connect to google ads and pull keyword data
// Make sure the drive file is shareable to the public
// Keep the sources for each industry average in case I'm asked

function pullResponses(currentEvent){
  const form = FormApp.openById('1GtXsmu9-eMD25wYVWhf6S44UkFxgpXwFCTqfcxVJ5iA');
  
  // Get the event object 'currentEvent', and pull all of the responses from the form
  var response = currentEvent.response;

  var responseList = [];

  // Loop through the current response and return the answers
  var itemResponses = response.getItemResponses();

  for (var i = 0; i < itemResponses.length; i++) {
    var itemResponse = itemResponses[i];
    // Push the responses into a list
    responseList.push(itemResponse.getResponse()); 
  }

  return responseList;
}

function generateSheet(){
  // Make sure to pull the spreadsheet ID from the url
  var templateId = '1o4SxUXpJEgYGpcCibcGpaC_l6fXRg_qTn4oZ4Yk4Zk0';
  var newName = 'Test Numbers Request';

  // Grab the numbers request template
  var templateFile = DriveApp.getFileById(templateId);
  var newFile = templateFile.makeCopy(newName);
  var newUrl = newFile.getUrl();

  // Use a regular expression to grab the spreadsheet ID from the URL
  var spreadsheetId = newUrl.match(/[-\w]{25,}/);
 
  return [spreadsheetId[0], newUrl];
}

function updateNumbers(e, id){
  var spreadSheetId = id;
  var spreadSheet = SpreadsheetApp.openById(spreadSheetId);
  var sheet = spreadSheet.getSheetByName('Budget Calculator');
  var responses = pullResponses(e);
  // Get the eCommerce answer so that the program can decide which variables to declare
  var isEcommerce = responses[7];

  if (isEcommerce == 'No') {
    var [amName, clientName, clientWebsite, budget, geoLocation, conversionRate, industry, isEcommerce, closeRate, clv] = responses;
    
    // If the client inputs a number greater than 1, then convert it into a decimal before placing in the sheet
    [conversionRate, closeRate] = convertToDecimals(conversionRate, closeRate);
    sheet.getRange("D6").setValue(budget);
    // Do the logic for getting cpc later
    sheet.getRange("D7").setValue(19);
    sheet.getRange("D9").setValue(conversionRate);
    sheet.getRange("C14").setValue(closeRate);
    sheet.getRange("C15").setValue(clv);
  } else {
    var [amName, clientName, clientWebsite, budget, geoLocation, conversionRate, industry, isEcommerce, avgOrderValue, purchaseFreq] = responses;
    console.log(avgOrderValue, purchaseFreq);
    sheet.getRange("D6").setValue(budget);
    // Do the logic for getting cpc later
    sheet.getRange("D7").setValue(19);
    sheet.getRange("D9").setValue(conversionRate);
    sheet.getRange("C14").setValue(closeRate);
    sheet.getRange("C15").setValue(clv);
  }

  spreadSheet.setName(clientName);
}

function convertToDecimals(conRate, clsRate){
  if (conRate >= 1){
    conRate = (conRate / 100);
  }
  if (clsRate >= 1){
    clsRate = (clsRate / 100);
  }

  return [conRate, clsRate];
}

function sendEmail(url){
  var draft = GmailApp.createDraft('christopher@smartsites.com', 'Numbers Request', url);
  var msg = draft.send();
  console.log(msg.getDate());
}

function myFunction(e) {
  var [spreadSheetId, newUrl] = generateSheet();
  updateNumbers(e, spreadSheetId);
  sendEmail(newUrl);
}

