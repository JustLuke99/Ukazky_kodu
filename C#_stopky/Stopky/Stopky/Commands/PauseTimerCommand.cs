using System.Diagnostics;
using System.Windows.Threading;

namespace Stopky.Commands;

public class PauseTimerCommand{
    private Stopwatch Timer;
    private DispatcherTimer Dispatcher;
    
    public PauseTimerCommand(Stopwatch timer, DispatcherTimer dispatcher){
        Timer = timer;
        Dispatcher = dispatcher;
    }
}