using System.Diagnostics;
using System.Windows.Threading;

namespace Stopky.Commands;

public class RestartTimerCommand: CommandBase{
    private Stopwatch Timer;
    private DispatcherTimer Dispatcher;
    private string TimePassed;
    
    public RestartTimerCommand(Stopwatch timer, DispatcherTimer dispatcher, string timePassed){
        Timer = timer;
        Dispatcher = dispatcher;
        TimePassed = timePassed;
    }
    
    public override void Execute(object? parameter){
        Timer.Stop();
        Timer.Reset();
        TimePassed = "00:00:00";
    }
    
}