# PasswordVault
A simple python-based password manager that encrypts login credentials using a key derived from a master username, password, and salt.

(I found this project that I did in the summer of 2014.)

WARNING: Even though this application makes use of common cryptographic algorithms such as AES-256 and SHA2, the security of this implementation has not been audited or verified and may contain security problems or otherwise be insecure for real-world use. All encrypted login credentials are stored locally and never uploaded to any server. Please do not rely on this program to protect sensitive information.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
