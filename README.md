# list of all available API endpoints
# App is hosted at this endpoint https://book-api-1234.herokuapp.com/. Use Http GET unless specified otherwise.

<ul>
  <li>/booklist/bookname/&ltname&gt</br>
  Example: <code>/booklist/bookname/the%20adventures</code> (%20 signifies space)
  </li>
</ul>

<ul>
  <li>/booklist/rent/</br>
  Example: <code>/booklist/rent/?lower=10&upper=100</code> (? signifies start of arguments. Please provide two arguments upper and lower)
  </li>
</ul>

<ul>
  <li>/booklist/custom/</br>
  Example: <code>/booklist/rent/?lower=10&upper=100&name=the&category=Fiction</code>
  </li>
</ul>

<ul>
  <li>/transactions/bookissue/</br> (use http POST)
  Example: The post body should contain these keys </br>
  <pre>
  {
    "book_name":"The Great Gatsby",
    "person_name":"ramesh"
  }
  </pre>
  </li>
</ul>

<ul>
  <li>/transactions/bookreturn/</br> (use http POST)
  Example: The post body should contain these keys </br>
  <pre>
  {
    "book_name":"The Great Gatsby",
    "person_name":"ramesh"
  }
  </pre>
  </li>
</ul>

<ul>
  <li>/transactions/person/$ltname&gt</br>
  Example: <code>/transactions/person/xyz</code>
  </li>
</ul>

<ul>
  <li>/transactions/generatedrent/$ltname&gt</br>
  Example: <code>/transactions/generatedrent/The%20Great%20Gatsby</code>
  </li>
</ul>

<ul>
  <li>/transactions/listofpeople/$ltname&gt</br>
  Example:<code> /transactions/listofpeople/The%20Great%20Gatsby</code>
  </li>
</ul>

<ul>
  <li>/transactions/daterange/</br>
  Example: <code>/transactions/listofpeople/?lower04/06/22=&upper=10/06/22</code> (provide these two arguments in format dd/mm/yy)
  </li>
</ul>
