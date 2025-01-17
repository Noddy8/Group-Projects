fetch('data.json')
  .then(response => response.json())
  .then(data => {
    quizData = data;
    loadQuestion();
  })
  .catch(error => console.error('Error loading quiz data:', error));

  
  let currentQuestionIndex = 0;
  let score = 0;
  
  const questionElement = document.getElementById('question');
  const optionsElement = document.getElementById('options');
  const resultElement = document.getElementById('result');
  const nextButton = document.getElementById('next-button');
  
  // Load the current question and options
  function loadQuestion() {
    const currentQuestion = quizData[currentQuestionIndex];
    questionElement.textContent = currentQuestion.question;
    optionsElement.innerHTML = '';
  
    currentQuestion.options.forEach(option => {
      const button = document.createElement('button');
      button.textContent = option;
      button.addEventListener('click', () => checkAnswer(option));
      optionsElement.appendChild(button);
    });
  }
  
  // Check the selected answer
  function checkAnswer(selectedOption) {
    const correctAnswer = quizData[currentQuestionIndex].answer;
  
    if (selectedOption === correctAnswer) {
      score++;
      resultElement.textContent = "Correct!";
    } else {
      resultElement.textContent = `Wrong! Correct answer is ${correctAnswer}`;
    }
  
    // Disable all buttons after selecting an answer //OPTIONAL
    const buttons = optionsElement.querySelectorAll('button');
    buttons.forEach(button => button.disabled = true);
  
    // Show the next button
    nextButton.style.display = 'block';
  }
  
  // Move to the next question
  nextButton.addEventListener('click', () => {
    currentQuestionIndex++;
  
    if (currentQuestionIndex < quizData.length) {
      loadQuestion();
      resultElement.textContent = '';
      nextButton.style.display = 'none';
    } else {
      showFinalResult();
    }
  });
  
  // Show the final score at the end
  function showFinalResult() {
    questionElement.textContent = `You scored ${score} out of ${quizData.length}`;
    optionsElement.innerHTML = '';
    nextButton.style.display = 'none';
  }
  
  loadQuestion();