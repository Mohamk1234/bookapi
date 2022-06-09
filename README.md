#list of all available API endpoints
#App is hosted at this endpoint https://book-api-1234.herokuapp.com/. Use Http GET unless specified otherwise.

<ul>
  <li>/booklist/bookname/&ltname&gt</br>
  Example: /booklist/bookname/the%20adventures (%20 signifies space)
  </li>
</ul>

<ul>
  <li>/booklist/rent/</br>
  Example: /booklist/rent/?lower=10&upper=100 (? signifies start of arguments. Please provide two arguments upper and lower)
  </li>
</ul>

<ul>
  <li>/booklist/custom/</br>
  Example: /booklist/rent/?lower=10&upper=100&name=the&category=Fiction 
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
