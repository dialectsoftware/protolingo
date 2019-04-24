# Cellular Automata

This demonstrates the flexibility of **protolingo** by using it to generate a configuration based [cellular automaton](http://mathworld.wolfram.com/ElementaryCellularAutomaton.html).
With this yaml configuration you can experiment with cellular automata without writing code. By just changing the configuration you can generate any elementary cellular automaton.


```bash
                                        #
                                       ###
                                      # # #
                                     ## # ##
                                    #   #   #
                                   ### ### ###
                                  # #   #   # #
                                 ## ## ### ## ##
                                #       #       #
                               ###     ###     ###
                              # # #   # # #   # # #
                             ## # ## ## # ## ## # ##
                            #   #       #       #   #
                           ### ###     ###     ### ###
                          # #   # #   # # #   # #   # #
                         ## ## ## ## ## # ## ## ## ## ##
                        #               #               #
                       ###             ###             ###
                      # # #           # # #           # # #
                     ## # ##         ## # ##         ## # ##
                    #   #   #       #   #   #       #   #   #
                   ### ### ###     ### ### ###     ### ### ###
                  # #   #   # #   # #   #   # #   # #   #   # #
                 ## ## ### ## ## ## ## ### ## ## ## ## ### ## ##
```

There are 256 variations you can explore. Modify the **chars** section specifying the characters you would like to use. Set the **rules** to the binary representation of any of the 256 variations. And set the generations to the number of iterations you would like. The output above was generated with the following configuration.

```yaml

-   config:
      exit_on_error : false
      chars : [' ', '#']
      rules : [1,0,0,1,0,1,1,0]
      generations : 50

```

There are 80 registers for console output, however, you can continue to add as many registers as necessary to get the desired output. The **id** for each register **must** be unique. The **bit** is the starting value for a cell. It must be a **0** or **1**. If you don't specify a bit one will be selected at random. The **neighbohood** defines the rules that will be used to calculate the next state of a cell given the value of the other cells in the neighborhood. The id of a neighbor must be the id of an existing register. The **depends_on** is used to ensure the cells are evaluated in order. For the fist cell depends_on can be either set to an empy array [] or itself.

```yaml

 - !register
      id: r0
      bit: 0
      neighborhood: [r79,r1]
      depends_on: [r0]

```

Here is another example, Rule 90.

```yaml
-   config:
      exit_on_error : false
      chars : [' ', '#']
      rules : [0,1,0,1,1,0,1,0]
      generations : 50

```

Console output:

```bash
                                        #
                                       # #
                                      #   #
                                     # # # #
                                    #       #
                                   # #     # #
                                  #   #   #   #
                                 # # # # # # # #
                                #               #
                               # #             # #
                              #   #           #   #
                             # # # #         # # # #
                            #       #       #       #
                           # #     # #     # #     # #
                          #   #   #   #   #   #   #   #
                         # # # # # # # # # # # # # # # #
                        #                               #
                       # #                             # #
                      #   #                           #   #
                     # # # #                         # # # #
                    #       #                       #       #
                   # #     # #                     # #     # #
                  #   #   #   #                   #   #   #   #
                 # # # # # # # #                 # # # # # # # #
                #               #               #               #
               # #             # #             # #             # #
              #   #           #   #           #   #           #   #
             # # # #         # # # #         # # # #         # # # #
            #       #       #       #       #       #       #       #
           # #     # #     # #     # #     # #     # #     # #     # #
          #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
         # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
```

