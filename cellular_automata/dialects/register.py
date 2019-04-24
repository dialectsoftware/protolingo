
 #  Copyright 2019  Dialect Software LLC or its affiliates. All Rights Reserved.
 #
 #  Licensed under the MIT License (the "License").
 #
 #  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 #  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 #  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 #  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 #  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 #  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 #  SOFTWARE.

import sys
import random
from protolingo.yaml.YAMLExpression import YAMLExpression

class Register(YAMLExpression):
    yaml_tag = u'!register'
    
    def __init__(self, id, depends_on, bit=None, neighborhood=None, output=None, exit=None, exitCode=None):
        super(Register, self).__init__(id, depends_on, output, exit, exitCode)
        if bit is None:
            self.bit = random.getrandbits(1)
        else:
            self.bit = bit  
        self.next = self.bit
        self.neighborhood = neighborhood
                      

    def exec(self,**kwargs):
        try:
            print(kwargs["config"]["chars"][self.bit], end='')
            if(len(self.neighborhood) == 2):
                yaml = kwargs["yaml"]
                key = "%s%s%s" % (yaml[self.neighborhood[0]].bit.get(), self.bit , yaml[self.neighborhood[1]].bit.get())
                index = int(key, 2)
                self.next = kwargs["config"]["rules"][::-1][index]
            sys.exit(0)
        except Exception as e:
            print(e.__str__())

    def reset(self):   
        super(Register, self).reset()
        self.bit = self.next

    def __repr__(self):
        return "%s(id=%r)" % (
            self.__class__.__name__, self.id)