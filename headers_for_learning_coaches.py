coach_with_strategies = i18n._("""
<div id="learning-tutor"><!-- begin learning tutor -->
    <p><!--the top-level message -->
        <table style="width: 100%; text-align:center;">
            <tr>
                <td><a href="#" class="show-subhint" data-subhint="unmotivated" data-hidden-text="Hide">[Feeling unmotivated?]</a>  </td>
                <td><a href="#" class="show-subhint" data-subhint="stuck" data-hidden-text="Hide">[Stuck?]</a></td>
                <td><a href="#" class="show-subhint" data-subhint="tips" data-hidden-text="Hide">[Want learning tips?]</a></td>
            </tr>
            </table>                        
    </p><!--end top-level message -->

    <!-- this is the dropdown text -->
    <div class="subhint" id="unmotivated">
        <p id="first-message">
            Remember, the harder you try, the more you grow your math brain!
        </p>
        <!-- request to learn more about motivational message -->
        <p>
            <a href="#" id="motivated-more" class="show-subhint" data-subhint="idea-1" data-hidden-text="Hide">[[More Ideas]]</a>
            <div class="subhint" id="idea-1" style="font-weight: bold;">
                <ul id="message-list">
                    <li>Remember, the more you practice the smarter you become!</li>
                    <li>When you learn a new kind of math problem, you grow your math brain!</li>
                    <li>If this is challenging, you have an opportunity to learn and become smarter!</li>
                    <li>Mistakes help you learn. Think hard to learn from them.</li>
                    <li>The more you learn today, the smarter you'll be tomorrow!</li>
                    <li>The harder you try the better you get!</li>
                    <li>Did you know... Your brain gets better the more you use it.</li>
                    <li>If you make a mistake, it's an opportunity to get smarter!</li>
                    <li>Your brain is like a muscle. The more you flex it, the more powerful it gets!</li>
                    <li>Thinking hard makes your brain grow stronger! Think hard about these math exercises.</li>
                    <li>Your brain grows new connections every time you practice. Help your brain grow more connections!</li>
                    <li>When you have to think harder, it makes you smarter!</li>
                    <li>Make your brain more powerful!  Practice hard!</li>
                    <li>Give your brain a workout.  The more you use it, the stronger it gets!</li>
                </ul>
            </div>    
        </p>
        <script type="text/javascript">
            //choose a random message from the list and display it at the top
            var mindsetList = document.getElementById('message-list');
            var messages = mindsetList.getElementsByTagName('li');
            var message = messages[Math.floor(Math.random() * messages.length)].innerHTML;
            document.getElementById('first-message').innerHTML = message;
        </script>
    </div>
    <!-- end link to request a motivational message & dropdown motivational message-->


                      
    <div class="subhint" id="stuck">
        <p>
            Sometimes it can help to ask yourself questions that help you reflect about your approach to the problem. Try the "What? Why? How?" 
            <span style="font-weight:bold">Reflect-on-Problem-Solving</span> strategy.
            Click on each word to see a question you can ask yourself while solving a problem.
        </p>
                                
        <table style="width: 100%; text-align:center;">
            <tr>
                <td><a href="#" class="show-subhint" data-subhint="what-problem-solving" style="font-weight: bold" data-hidden-text="Hide">
                    What?</a> </td>
                <td><a href="#" class="show-subhint" data-subhint="why-problem-solving" style="font-weight: bold" data-hidden-text="Hide">
                    Why?</a> </td>
                <td> <a href="#" class="show-subhint" data-subhint="how-problem-solving" style="font-weight: bold" data-hidden-text="Hide">
                    How?</a></td>
            </tr>
        </table>
                                
                            
        <div class="subhint" style="font-weight: bold" id="what-problem-solving">
            What are you doing or thinking right now?</div>
                       
        <div class="subhint" style="font-weight: bold" id="why-problem-solving">
            Why is what you are currently doing helpful?
            Why is it useful for achieving your goal?</div>

        <div class="subhint" style="font-weight: bold" id="how-problem-solving">
            How well is your current approach to this problem
            working?</div>
        <br>
        <br>
        <a href="#" class="show-subhint" data-subhint="encouragement" data-hidden-text="Hide Information">
            What if I can’t do it?</a>
        <div class="subhint" id="encouragement">
            Many students are not sure what to say, or think
            their answer isn’t good. That is fine, as long as you
            <span style="font-weight: bold; font-style:italic">try</span>
            to think about the question, by typing or saying the
            answer to yourself.
        </div>
    </div>
    <!-- end link to request a Problem Solving Strategy & dropdown strategy-->

    <div class="subhint" id="tips">
        <p>
            Sometimes it can help to ask yourself questions that help you reflect about your understanding of the problem. 
            Try the  "What? Why? How?" <span style="font-weight:bold">Reflect-on-Understanding</span> strategy.
            Click on each word to see a question you can ask yourself while solving a problem.
        </p>
                            
        <table style="width: 100%; text-align:center;">
            <tr>
                <td><a href="#" class="show-subhint" data-subhint="what-problem-understanding" style="font-weight: bold" data-hidden-text="Hide">
                What?</a> </td>
                <td><a href="#" class="show-subhint" data-subhint="why-problem-understanding" style="font-weight: bold" data-hidden-text="Hide">
                Why?</a> </td>
                <td> <a href="#" class="show-subhint" data-subhint="how-problem-understanding" style="font-weight: bold" data-hidden-text="Hide">
                How?</a></td>
            </tr>
        </table>
                                
                            
        <div class="subhint" style="font-weight: bold" id="what-problem-understanding">
            What does this step mean to you?</div>
                       
        <div class="subhint" style="font-weight: bold" id="why-problem-understanding">
            Why is it helpful to take this step?</div>

        <div class="subhint" style="font-weight: bold" id="how-problem-understanding">
            How do you know this step is right?</div>
        <br>
        <br>
        <a href="#" class="show-subhint" data-subhint="encouragement-understanding" data-hidden-text="Hide Information">
            What if I can’t do it?</a>

        <div class="subhint" id="encouragement-understanding">
            Many students are not sure what to say, or think
            their answer isn’t good. That is fine, as long as you
            <span style="font-weight: bold; font-style:italic">try</span>
            to think about the question, by typing or saying the
            answer to yourself.
        </div>
    </div>                         
</div>
""")



coach_with_lists = i18n._("""
<div id="learning-tutor"><!-- begin learning tutor -->
    <p><!--the top-level message -->
        <table style="width: 100%; text-align:center;">
            <tr>
                <td><a href="#" class="show-subhint" data-subhint="unmotivated" data-hidden-text="Hide">[Feeling unmotivated?]</a>  </td>
                <td><a href="#" class="show-subhint" data-subhint="stuck" data-hidden-text="Hide">[Stuck?]</a></td>
                <td><a href="#" class="show-subhint" data-subhint="tips" data-hidden-text="Hide">[Want learning tips?]</a></td>
            </tr>
            </table>                        
    </p><!--end top-level message -->

    <!-- this is the dropdown text -->
    <div class="subhint" id="unmotivated">
        <p id="first-message">
            Remember, the harder you try, the more you grow your math brain!
        </p>
        <!-- request to learn more about motivational message -->
        <p>
            <a href="#" id="motivated-more" class="show-subhint" data-subhint="idea-1" data-hidden-text="Hide">[[More Ideas]]</a>
            <div class="subhint" id="idea-1" style="font-weight: bold;">
                <ul id="message-list">
                    <li>Remember, the more you practice the smarter you become!</li>
                    <li>When you learn a new kind of math problem, you grow your math brain!</li>
                    <li>If this is challenging, you have an opportunity to learn and become smarter!</li>
                    <li>Mistakes help you learn. Think hard to learn from them.</li>
                    <li>The more you learn today, the smarter you'll be tomorrow!</li>
                    <li>The harder you try the better you get!</li>
                    <li>Did you know... Your brain gets better the more you use it.</li>
                    <li>If you make a mistake, it's an opportunity to get smarter!</li>
                    <li>Your brain is like a muscle. The more you flex it, the more powerful it gets!</li>
                    <li>Thinking hard makes your brain grow stronger! Think hard about these math exercises.</li>
                    <li>Your brain grows new connections every time you practice. Help your brain grow more connections!</li>
                    <li>When you have to think harder, it makes you smarter!</li>
                    <li>Make your brain more powerful!  Practice hard!</li>
                    <li>Give your brain a workout.  The more you use it, the stronger it gets!</li>
                </ul>
            </div>    
        </p>
        <script type="text/javascript">
            //choose a random message from the list and display it at the top
            var mindsetList = document.getElementById('message-list');
            var messages = mindsetList.getElementsByTagName('li');
            var message = messages[Math.floor(Math.random() * messages.length)].innerHTML;
            document.getElementById('first-message').innerHTML = message;
        </script>
    </div>
    <!-- end link to request a motivational message & dropdown motivational message-->


                      
    <div class="subhint" id="stuck">
        <p id="first-message-2">
            Remember, the harder you try, the more you grow your math brain!
        </p>
        <!-- request to learn more about motivational message -->
        <p>
            <a href="#" id="motivated-more-2" class="show-subhint" data-subhint="idea-1-2" data-hidden-text="Hide">[[More Ideas]]</a>
            <div class="subhint" id="idea-1-2" style="font-weight: bold;">
                <ul id="message-list-2">
                    <li>Remember, the more you practice the smarter you become!</li>
                    <li>When you learn a new kind of math problem, you grow your math brain!</li>
                    <li>If this is challenging, you have an opportunity to learn and become smarter!</li>
                    <li>Mistakes help you learn. Think hard to learn from them.</li>
                    <li>The more you learn today, the smarter you'll be tomorrow!</li>
                    <li>The harder you try the better you get!</li>
                    <li>Did you know... Your brain gets better the more you use it.</li>
                    <li>If you make a mistake, it's an opportunity to get smarter!</li>
                    <li>Your brain is like a muscle. The more you flex it, the more powerful it gets!</li>
                    <li>Thinking hard makes your brain grow stronger! Think hard about these math exercises.</li>
                    <li>Your brain grows new connections every time you practice. Help your brain grow more connections!</li>
                    <li>When you have to think harder, it makes you smarter!</li>
                    <li>Make your brain more powerful!  Practice hard!</li>
                    <li>Give your brain a workout.  The more you use it, the stronger it gets!</li>
                </ul>
            </div>    
        </p>
        <script type="text/javascript">
            //choose a random message from the list and display it at the top
            var mindsetList = document.getElementById('message-list-2');
            var messages = mindsetList.getElementsByTagName('li');
            var message = messages[Math.floor(Math.random() * messages.length)].innerHTML;
            document.getElementById('first-message-2').innerHTML = message;
        </script>
    </div>
    <!-- end link to request a Problem Solving Strategy & dropdown strategy-->

    <div class="subhint" id="tips">
        <p id="first-message-3">
            Remember, the harder you try, the more you grow your math brain!
        </p>
        <!-- request to learn more about motivational message -->
        <p>
            <a href="#" id="motivated-more-3" class="show-subhint" data-subhint="idea-1-3" data-hidden-text="Hide">[[More Ideas]]</a>
            <div class="subhint" id="idea-1-3" style="font-weight: bold;">
                <ul id="message-list">
                    <li>Remember, the more you practice the smarter you become!</li>
                    <li>When you learn a new kind of math problem, you grow your math brain!</li>
                    <li>If this is challenging, you have an opportunity to learn and become smarter!</li>
                    <li>Mistakes help you learn. Think hard to learn from them.</li>
                    <li>The more you learn today, the smarter you'll be tomorrow!</li>
                    <li>The harder you try the better you get!</li>
                    <li>Did you know... Your brain gets better the more you use it.</li>
                    <li>If you make a mistake, it's an opportunity to get smarter!</li>
                    <li>Your brain is like a muscle. The more you flex it, the more powerful it gets!</li>
                    <li>Thinking hard makes your brain grow stronger! Think hard about these math exercises.</li>
                    <li>Your brain grows new connections every time you practice. Help your brain grow more connections!</li>
                    <li>When you have to think harder, it makes you smarter!</li>
                    <li>Make your brain more powerful!  Practice hard!</li>
                    <li>Give your brain a workout.  The more you use it, the stronger it gets!</li>
                </ul>
            </div>    
        </p>
        <script type="text/javascript">
            //choose a random message from the list and display it at the top
            var mindsetList = document.getElementById('message-list-3');
            var messages = mindsetList.getElementsByTagName('li');
            var message = messages[Math.floor(Math.random() * messages.length)].innerHTML;
            document.getElementById('first-message-3').innerHTML = message;
        </script>
    </div>
                           
</div>
""")