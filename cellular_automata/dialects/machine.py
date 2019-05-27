
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
from protolingo.utils import marshal_output
from protolingo.yaml.Parser import Parser
from protolingo.yaml.YAMLExpression import YAMLExpression

class Machine(YAMLExpression):
    yaml_tag = u'!machine'
    def __init__(self, id, depends_on, registers, output=None, exit=None, exitCode=None, **kwargs):
        super(Machine, self).__init__(id, depends_on, output, exit, exitCode)
        self.registers = registers
        

    def exec(self,**kwargs):
        try:
            Parser.resolve_ref_all(self.registers, **kwargs)
            for i in range(kwargs["config"]["generations"]):
                for register in self.registers:
                    output = Parser.comprehend(register, **kwargs)
                    marshal_output(output)
                print("")
                [r.proxy.reset() for r in self.registers]
            sys.exit(0)
        except Exception as e:
            raise
 
    def __repr__(self):
        return "%s(id=%r)" % (
            self.__class__.__name__, self.id)