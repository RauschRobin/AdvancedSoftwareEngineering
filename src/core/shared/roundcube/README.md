# RoundcubeMock Class

This Python code defines a class named `RoundcubeMock`, which serves as a mock of the Roundcube email API. The class provides methods to simulate checking for new emails and retrieving the last received email. It also includes a list of example emails for demonstration purposes.

## Class Methods

### `__init__(self)`

The class constructor (`__init__`) takes no parameters and initializes the class. As the constructor is empty, it doesn't perform any specific actions during instantiation.

### `checkForNewEmail(self)`

This method simulates checking the email account for new emails. If there is a new email (determined randomly), it returns a random email from the `example_emails` list. The randomness is introduced using the `random.randint(0, 9)` function. If the result is equal to 3, a random email is selected and returned.

**Parameters:** None
**Returns:** None or a random email (string)

### `getLastReceivedEmail(self)`

This method returns a random email as the last received email. It simply retrieves the first email from the `example_emails` list.

**Parameters:** None
**Returns:** Random email (string)

## Example Emails

The `example_emails` list contains strings that represent example email messages. These messages cover various scenarios such as professor announcements, lecture cancellations, event invitations, and more. These example emails are used by the `RoundcubeMock` methods to simulate email interactions.
