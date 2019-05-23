Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1
Sub GetLinks()
Set objIE = CreateObject("InternetExplorer.Application")
objIE.Top = 0
objIE.Left = 0
objIE.Width = 800
objIE.Height = 600
objIE.AddressBar = 1
objIE.StatusBar = 1
objIE.Toolbar = 1
objIE.Visible = True 'Show IE Window while testing

objIE.Navigate ("site")  'Specify website to scrape
Do
DoEvents
Loop Until objIE.ReadyState = 4

Row = 0
     
    'Search for classes with specified name 
    For Each link In objIE.Document.getElementsbyClassName("Link")

    'Fill spreadsheet
    'If (link.className = strn) Then
        Worksheets(1).Range("A" & Row + 2).Value = Row
        Worksheets(1).Range("B" & Row + 2).Value = link.className
        Worksheets(1).Range("C" & Row + 2).Value = link.ID
        Worksheets(1).Range("D" & Row + 2).Value = link.tagName
        'Worksheets(1).Range("E" & Row + 2).Value = link.Name
        'Worksheets(1).Range("F" & Row + 2).Value = link.Type
        Worksheets(1).Range("G" & Row + 2).Value = link.href
        Worksheets(1).Range("H" & Row + 2).Value = link.innertext
        
  'End If
  Row = Row + 1

Next link



'Then loop through links scraped from above for more info
      
counter = 0

mylabel:


'Grab sub-page to scrape
website = Worksheets(1).Range("G" & counter + 2)

objIE.Navigate (website)

Do
DoEvents
Loop Until objIE.ReadyState = 4

Row = 0
Dim strn As String

'Search for donwload links on specified page and save to spreadsheet
strn = " Download"
     
For Each link In objIE.Document.getElementsbyTagName("a")

 If (link.innertext = strn) Then
    Worksheets(2).Range("A" & counter + 2).Value = Row
    Worksheets(2).Range("G" & counter + 2).Value = link.href
    Worksheets(2).Range("H" & counter + 2).Value = link.innertext
    Row = Row + 1
  End If
  
Next link
    
counter = counter + 1

If (counter < 101) Then GoTo mylabel
      
objIE.Quit
Set objIE = Nothing

