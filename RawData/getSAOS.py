import sys

corpse = """
<script>
   $(function(){

      $("#scooterJudgmentsButton").click(function() {

         $.ajax({
            method: "GET",
            url: "%s"
         })
         .done(function(data) {
            for (var i=0; i<data.items.length; i++) {
               var judgment = data.items[i];
               $("#scooterJudgments").append("<li><a href='https://www.saos.org.pl/judgments/"+judgment.id+"'>"+judgment.judgmentDate+", "+judgment.courtCases[0].caseNumber+", " + judgment.division.court.name+"</a>"
                                            + "<p>..."+judgment.textContent+"...</p>"
                                            +"</li>");
        }
        $("#scooterJudgmentsButton").remove();

     });
     });

  });
</script>

<h5>Ozeczenia zwiazane z klauzula w bazie SAOS</h5>
<button id="scooterJudgmentsButton">Wyswietl</button>

<ul id="scooterJudgments">
</ul>
"""


def getSOASjQuery(tom, sad, numer, rok):
    """wszystko ma byc stringami"""
    urlTemplate = "https://www.saos.org.pl/search?signature=%s&all=%s&size=20&sort=JUDGMENT_DATE%%2Cdesc"
    textSearch = "%s+%s+%s%%2F%s" % (tom, sad, numer, rok)
    url = urlTemplate % (textSearch, textSearch)
    return url

if __name__ == "__main__":
    print getSOASjQuery('VI', 'ACa', '1114', '13')
    pass
