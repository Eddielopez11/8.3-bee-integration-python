from bottle import route, run, static_file, get

@route('/')
def skaters():
    return '''
    <head>
    <meta charset="utf-8">
    <title>summer16-1.4-css</title>
    <link rel="stylesheet" href="static/main.css">
  </head>
  <body>
    <div class="body">
      <header>

      <!-- Navigation for social media -->
      <nav class="nav__socialMediaMain">
        <div class="container">
          <a href="#subscribe" class="nav__subscribe">
              subscribe
          </a>
            <a href="#facebook">
              <img class="nav__facebook" src="http://www.freeiconspng.com/uploads/facebook-f-logo-png-home-find-us-on-facebook-25.png" alt="Facebook logo" />
            </a>
            <a href="#rssFeed">
              <img  class="nav__rssFeed" src="http://www.freeiconspng.com/uploads/rss-logo-icon-png-4.png" alt="RSS FEED logo" />
            </a>
            <a href="#twitter">
              <img  class="nav__twitter" src="https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Twitter_bird_logo_2012.svg/1259px-Twitter_bird_logo_2012.svg.png" alt="Twitter logo" />
            </a>
            <a href="#youtube">
              <img  class="nav__youtube" src="http://2012.igem.org/wiki/images/e/ea/Youtube-logo-2.png" alt="Youtube logo" />
            </a>
          </div>
        </nav>

       <!-- Navigtion for main website bar -->
        <nav class="nav__bar">
          <a href="#sk8tNews" class="nav__bar--color">sk8t news</a>
          <a href="#skateboards" class="nav__bar--color">skateboards</a>
          <a href="#boardDesign" class="nav__bar--color">board design</a>
          <a href="#contactUs" class="nav__bar--color">contact us</a>
        </nav>
      </header>
      <main>
        <div class="main__image--div">
          <a href="#powellPeralta">
            <img class="main__image--resize" src="assets/top-image.png" alt="powell peralta skateboards" />
          <img class="main__image--grid" src="assets/grid.png" alt="" />
          <img class="main__image--logo" src="assets/peralta-logo.png" alt="" />
          </a>
        </div>
          <a href="#powellPeralta">
          </a>
          <a href="#carouselImage2">
          </a>
          <a href="#carouselImage3">
          </a>
      </main>
      <section class="grid__row">
        <div class="grid__column">
          <article class="article">
            <h2>
                tony hawk foundation raises big money at celeb fundraiser
            </h2>
            <time datetime="2013-10-10T05:00">October 10, 2013</time>
            <p>
              It was just over 90 degrees in Los Angeles, but that didn't stop the throngs from comming out to celebrate the 10th Annual Tony Hawk's Stand Up For Skateparks Benefit Presented by SLS Hotels & Casino Las Vegas on Saturday at the Green Acres Estate in Beverly Hills.
            </p>
            <a class="article__readMore" href="#tonyHawksFoundation">[read more]</a>
          </article>
        </div>
        <div class="grid__column">
          <article class="">
            <h2>
                rodney mullen: pop an ollie and innovate! (TED talks)
            </h2>
            <time datetime="2013-3-10T06:00">March 10, 2013</time>
            <p>
              The last thing Rodney Mullen, the godfather of street skating, wanted were competitive victories. In this exuberant talk he shares his love of the open skateboarding community and how the unique enviroments it plays in drive the creation of new tricks -- fostering...
            </p>
            <a class="article__readMore" href="#RodneyMullen">[read more]</a>
          </article>
        </div>
        <div class="grid__column">
          <article class="">
            <h2>
              ray barbee talks 'ban this'
            </h2>
            <time datetime="2013-10-4T08:00">October 4, 2013</time>
            <p>
              Since filming is in full swing for the Vans video Adventures With Chris has taken the opportunity to sit some of the team down to look behind the skating of some of their earlier parts. Today we sit down Ray Barbee, one of the smoothest guys to ever step on skateboard and Chris' childhood idol...
            </p>
            <a class="article__readMore" href="#rayBarbee">[read more]</a>
          </article>
        </div>
      </section>
      <section>
          <!-- images below articles -->
          <div class="contact__div--names">
            <a href="#lanceMountain">
              <img class="sk8er__resize--topLeft" src="assets/sk8er-4.png" alt="lance mountain" />
              <h3 class="sk8er__names">lance mountain</h3>
            </a>
          </div>
          <div class="contact__div--names">
            <a href="#rodneyMullen">
              <img class="sk8er__resize--topMid" src="assets/sk8er-3.png" alt="rodney mullen" />
              <h3 class="sk8er__names">rodney mullen</h3>
            </a>
          </div>
          <div class="contact__div--names">
            <a href="#steveCaballero">
              <img class="sk8er__resize--topRight" src="assets/sk8er-2.png" alt="steve caballero" />
              <h3 class="sk8er__names">steve caballero</h3>
            </a>
          </div>
          <div class="contact__div--names">
            <a href="#tommyGuerrero">
              <img class="sk8er__resize--bottomLeft" src="assets/sk8er-1.png" alt="tommy guerrero" />
              <h3 class="sk8er__names">tommy guerrero</h3>
            </a>
          </div>
      </section>
      <section class="sk8boards__color">

        <!-- skateboards -->
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-3.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-4.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-5.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-6.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-7.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-8.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-9.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-10.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-2.png" alt="" />
        </a>
        <a href="#">
          <img class="sk8boards__alignWithin" src="assets/sk8-1.png" alt="" />
        </a>
      </section>
      <footer class="contact__color">
        <div class="contact__leftAlign">
          <h2>
            Contact Us for More Information
          </h2>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elite. Aliquam semper nulla ut odio scelerisque varius. Phasellus dui nunc, lacinia at vehicula congue, vehicula nec tellus. Morbi dignissim rutrum lorem at tincidunt.
          </p>
          <a href="#facebook">
            <img class="contact__facebook" src="http://www.freeiconspng.com/uploads/facebook-f-logo-png-home-find-us-on-facebook-25.png" alt="Facebook logo" />
          </a>
          <a href="#rssFeed">
            <img class="contact__rssFeed" src="http://www.freeiconspng.com/uploads/rss-logo-icon-png-4.png" />
          </a>
          <a href="#twitter">
            <img class="contact__twitter" src="https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Twitter_bird_logo_2012.svg/1259px-Twitter_bird_logo_2012.svg.png" alt="Twitter logo" />
          </a>
          <a href="#youtube">
            <img class="contact__youtube" src="http://2012.igem.org/wiki/images/e/ea/Youtube-logo-2.png" />
          </a>
        </div>
        <div class="contact__rightAlign">
          <form class="" action="index.html" method="post">
            <input class="contact__inputName" type="text" name="name" value="name">
            <input class="contact__inputEmail" type="text" name="email" value="email">
            <textarea class="contact__inputTextArea" name="text" rows="8" cols="40"></textarea>
            <input class="contact__submit" type="submit" name="submit" value="Submit">
          </form>
        </div>
      </footer>
    </div>
  </body>
    '''

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@get('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets')



run(host='localhost', port=8080, debug=True)
