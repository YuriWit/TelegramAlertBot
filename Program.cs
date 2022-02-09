using Telegram.Bot;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Extensions.Polling;
using Telegram.Bot.Types;
using Telegram.Bot.Types.Enums;

using CoinGecko.Clients;
using CoinGecko.Interfaces;

using System.Threading;


// Get telegram api key from .key file
string path = @".\telegram.key";
if (!System.IO.File.Exists(path))
    throw new InvalidOperationException("No telegram.key file.");
string telegramKey = System.IO.File.ReadAllText(path);

// start bot client
var botClient = new TelegramBotClient(telegramKey);


using var cts = new CancellationTokenSource();

// StartReceiving does not block the caller thread. Receiving is done on the ThreadPool.
var receiverOptions = new ReceiverOptions
{
    AllowedUpdates = { } // receive all update types    
};
botClient.StartReceiving(
    HandleUpdateAsync,
    HandleErrorAsync,
    receiverOptions,
    cancellationToken: cts.Token);

var me = await botClient.GetMeAsync();

Console.WriteLine($"Start listening for @{me.Username}");



///////////////////
ICoinGeckoClient _client;
_client = CoinGeckoClient.Instance;
const string ids = "bitcoin";
const string vsCurrencies = "usd";
var result = await _client.SimpleClient.GetSimplePrice(new []{ids},new []{vsCurrencies});
Console.WriteLine(result[ids][vsCurrencies].ToString());
////////////////////

// loop btc price
int millisecondsTimeout = 1000*10;
while(true){
    result = await _client.SimpleClient.GetSimplePrice(new []{ids},new []{vsCurrencies});
    Console.WriteLine(result[ids][vsCurrencies].ToString());
    if(result[ids][vsCurrencies] > 40000)
    {
        Message sentMessage = await botClient.SendTextMessageAsync(
            chatId: 2113705847,
            text: "BTC is " + result[ids][vsCurrencies] + " usd");
    }
    Thread.Sleep(millisecondsTimeout);
}
//



Console.ReadLine();

// Send cancellation request to stop bot
cts.Cancel();

async Task HandleUpdateAsync(ITelegramBotClient botClient, Update update, CancellationToken cancellationToken)
{
    // Only process Message updates: https://core.telegram.org/bots/api#message
    if (update.Type != UpdateType.Message)
        return;
    // Only process text messages
    if (update.Message!.Type != MessageType.Text)
        return;

    var chatId = update.Message.Chat.Id;
    var messageText = update.Message.Text;

    Console.WriteLine($"Received a '{messageText}' message in chat {chatId}.");

    // Echo received message text
    Message sentMessage = await botClient.SendTextMessageAsync(
        chatId: chatId,
        text: "You said:\n" + messageText,
        cancellationToken: cancellationToken);
}

Task HandleErrorAsync(ITelegramBotClient botClient, Exception exception, CancellationToken cancellationToken)
{
    var ErrorMessage = exception switch
    {
        ApiRequestException apiRequestException
            => $"Telegram API Error:\n[{apiRequestException.ErrorCode}]\n{apiRequestException.Message}",
        _ => exception.ToString()
    };

    Console.WriteLine(ErrorMessage);
    return Task.CompletedTask;
}
