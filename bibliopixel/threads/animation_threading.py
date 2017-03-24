import threading, time
from .. import log


class AnimationThreading(object):
    """
    AnimationThreading handles threading - and eventually multiprocessing - for
    BaseAnimation.
    """

    def __init__(self, animation, threaded, join_thread):
        self.animation = animation
        self.threaded = threaded
        self.join_thread = join_thread
        self.stop_event = threading.Event()
        self.thread = None

    def report_framerate(self, start, mid, now):
        stepTime = int(mid - start)
        render_duration = int(now - mid)
        totalTime = stepTime + render_duration
        fps = int(1.0 / max(totalTime, 1))
        log.debug("%sms/%sfps / Frame: %sms / Update: %sms",
                  totalTime, fps, stepTime, render_duration)

    def stop_thread(self, wait=False):
        if self.thread:
            self.stop_event.set()
            if wait:
                self.thread.join()

    def stopped(self):
        return not (self.thread and self.thread.isAlive())

    def wait(self, t):
        if self.threaded:
            self.stop_event.wait(t)
        else:
            time.sleep(t)

    def run_animation(self, run):
        if not self.threaded:
            run()
            return

        def target():
            # TODO: no testpath exercises this code...
            log.debug('Starting thread...')
            run()
            log.debug('Thread Complete')

        self.stop_event.clear()

        self.thread = threading.Thread(target=target, daemon=True)
        self.thread.start()

        if self.join_thread:
            # TODO: why would you do this rather than disable threading?
            self.thread.join()